from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Image, Informacion

def index(request):
    home_info = Informacion.objects.first()
    if home_info:
        print(type(home_info))
        return render(request, 'index.html', context={'home': home_info})
    else:
        return render(request, 'index.html')

def imagenes(request):
    images = Image.objects.order_by('-calificacion')
    images_json = serializers.serialize('json', images)
    return HttpResponse(images_json, content_type='application/json')

def galeria(request):
    return render(request, 'galeria.html')
