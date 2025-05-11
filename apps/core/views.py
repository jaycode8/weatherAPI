from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.cache import cache
from apps.core.services import get_data

# Create your views here.

@api_view(["GET"])
def weather(request):
    location = request.GET.get('location', '')
    if cache.get(location):
        print("data from redis")
        data = cache.get(location)
    else:
        try:
            print("data from api")
            data = get_data(location)
            cache.set(location, data, 1800)
        except:
            data = {}
    if not location:
        data = {}

    return render(request, "index.html", data)
