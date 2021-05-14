from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from BetterTube.youtube_api_integration import get_most_popular_videos_in_region, get_authorization_url


def index(request):
    return render(request, "build/index.html")

def home(request):
    if request.user.is_authenticated:
        pass
    else:
        return JsonResponse(get_most_popular_videos_in_region("US"), safe=False)

def get_user_data(request):
    if request.user.is_authenticated:
        return JsonResponse({'avatar': request.user.avatar_url, 'name': request.user.first_name + ' ' + request.user.last_name})
    else:
        return HttpResponse(status=401)


def request_authorization_url(request):
    return JsonResponse({'authorization_url': get_authorization_url()})