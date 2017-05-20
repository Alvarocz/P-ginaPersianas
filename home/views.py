from django.shortcuts import render
from django.http import HttpResponse
from home.models import Image

def index(request):
    return render(request, 'index.html')

def galeria(request):
    images = Image.objects.order_by('-calificacion')
    return render(request, 'galeria.html', context={'images': images})
