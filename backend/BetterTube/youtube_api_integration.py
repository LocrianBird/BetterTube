import os
from decimal import Decimal

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import dateutil.parser
from google.auth.transport import requests
from google.oauth2 import id_token
from isoduration import parse_duration

scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/userinfo.profile",
          "https://www.googleapis.com/auth/userinfo.email"]

client_secrets_file = "google_secret.json"


def get_client_secret():
    f = open(client_secrets_file, "w+", encoding='utf-8')
    f.write(os.environ["google_secret"])
    f.close()


def verify_token_and_return_userdata(token, client_id):
    return id_token.verify_oauth2_token(token, requests.Request(), client_id)


def get_authorization_url():
    get_client_secret()
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        client_secrets_file,
        scopes=scopes)
    flow.redirect_uri = 'http://localhost:8000/signin/'
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    os.remove(client_secrets_file)
    return authorization_url, state


def get_profile_data():
    user_info_service = googleapiclient.discovery.build(
        serviceName='oauth2', version='v2',
        developerKey=os.environ["developerKey"])
    user_info = user_info_service.userinfo().get().execute()
    if user_info and user_info.get('id'):
        return user_info


def exchange_url_for_tokens(url, state):
    get_client_secret()
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        client_secrets_file,
        scopes=None,
        state=state)
    flow.redirect_uri = 'http://localhost:8000/signin/'
    flow.fetch_token(authorization_response=url)
    os.remove(client_secrets_file)
    return flow.credentials


def get_most_popular_videos_in_region(region):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    get_client_secret()

    # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #  client_secrets_file, scopes)
    # credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=os.environ["developerKey"])

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode=region,
        maxResults=50
    )
    response = request.execute()

    def duration_to_string(duration):
        if duration.hours == Decimal(0):
            return f"{duration.minutes}:{duration.seconds}"
        return f"{duration.hours}:{duration.minutes}:{duration.seconds}"

    os.remove(client_secrets_file)

    return [{"thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
             "caption": item["snippet"]["title"],
             "link": f"https://www.youtube.com/watch?v={item['id']}",
             "time": duration_to_string(parse_duration(item["contentDetails"]["duration"]).time),
             "timeposted": dateutil.parser.parse(item["snippet"]["publishedAt"]).strftime('%d %b %Y'),
             "creator": item["snippet"]["channelTitle"]
             } for item in response['items']]


if __name__ == "__main__":
    print(get_profile_data())
