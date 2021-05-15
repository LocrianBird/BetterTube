from django.contrib.auth import login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from BetterTube.models import User
from BetterTube.youtube_api_integration import get_most_popular_videos_in_region, get_authorization_url, \
    exchange_url_for_tokens, verify_token_and_return_userdata


def index(request):
    return render(request, "build/index.html")

def home(request):
    if request.user.is_authenticated:
        return HttpResponse(status=204)
    else:
        return JsonResponse(get_most_popular_videos_in_region("US"), safe=False)

def get_user_data(request):
    if request.user.is_authenticated:
        return JsonResponse({'avatar': request.user.avatar_url, 'name': request.user.first_name + ' ' + request.user.last_name})
    else:
        return HttpResponse(status=401)


def request_authorization_url(request):
    authorization_url, state = get_authorization_url()
    response = JsonResponse({'authorization_url': authorization_url})
    response.set_cookie("state", state, domain="localhost:8000", secure=True, httponly=True)
    return response

def signin(request):
    state = request.COOKIES.get("state")
    credentials = exchange_url_for_tokens(request.build_absolute_uri(), state)
    userdata = verify_token_and_return_userdata(credentials.id_token, credentials.client_id)
    user_id = userdata["sub"]
    try:
        user = User.objects.get(pk=user_id)
    except:
        user = User()
        user.user_id = user_id
        user.access_token = credentials.token
        user.id_token = credentials.id_token
        user.refresh_token = credentials.refresh_token
        user.avatar_url = userdata["picture"]
        user.first_name = userdata["given_name"]
        user.last_name = userdata["family_name"]
        user.email = userdata["email"]
        user.save()
    login(request, user)
    return redirect('/')

