# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from home import views as homeviews

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$', homeviews.index, name='index'),
    url(r'^getimages', homeviews.images, name='images'),
    url(r'^getvideos', homeviews.videos, name='videos'),
    url(r'^galeria', homeviews.galeria, name='galeria'),
    url(r'^videos', homeviews.galeria_videos, name='galeria_videos'),
]
