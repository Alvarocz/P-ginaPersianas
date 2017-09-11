from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Image, Video, Informacion

def index(request):
    home_info = Informacion.objects.first()
    if home_info:
        print(type(home_info))
        return render(request, 'index.html', context={'home': home_info})
    else:
        return render(request, 'index.html')

def images(request):
    images = Image.objects.order_by('-calificacion')
    images_json = serializers.serialize('json', images)
    return HttpResponse(images_json, content_type='application/json')
  
def videos(request):
    videos = Video.objects.all()
    videos_json = serializers.serialize('json', videos)
    return HttpResponse(videos_json, content_type='application/json')

def galeria(request):
    return render(request, 'galeria.html')

def galeria_videos(request):
    return render(request, 'videos.html')
