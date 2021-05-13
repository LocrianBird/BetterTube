from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, "build/index.html")

def recommendations(request):
    recom_array = [{"thumbnail": "https://i.ytimg.com/vi/DHPf_b7T9_M/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD-4iMY2A0yLu7gYseOr_Gg1x3YGg",
             "caption": "my roommates cat bites my foot and dies",
             "link": "https://www.youtube.com/watch?v=DHPf_b7T9_M",
            },
            {
                "thumbnail": "https://i.ytimg.com/vi/DHPf_b7T9_M/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD-4iMY2A0yLu7gYseOr_Gg1x3YGg",
                "caption": "my roommates cat bites my foot and dies",
                "link": "https://www.youtube.com/watch?v=DHPf_b7T9_M",
            },
            {
                "thumbnail": "https://i.ytimg.com/vi/DHPf_b7T9_M/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD-4iMY2A0yLu7gYseOr_Gg1x3YGg",
                "caption": "my roommates cat bites my foot and dies",
                "link": "https://www.youtube.com/watch?v=DHPf_b7T9_M",
            },
            {
                "thumbnail": "https://i.ytimg.com/vi/DHPf_b7T9_M/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD-4iMY2A0yLu7gYseOr_Gg1x3YGg",
                "caption": "my roommates cat bites my foot and dies",
                "link": "https://www.youtube.com/watch?v=DHPf_b7T9_M",
            },
            {
                "thumbnail": "https://i.ytimg.com/vi/DHPf_b7T9_M/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD-4iMY2A0yLu7gYseOr_Gg1x3YGg",
                "caption": "my roommates cat bites my foot and dies",
                "link": "https://www.youtube.com/watch?v=DHPf_b7T9_M",
            }
            ]
    return JsonResponse(recom_array, safe=False)