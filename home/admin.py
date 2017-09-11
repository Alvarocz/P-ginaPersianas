# -*- coding: utf-8 -*-
from django.contrib import admin
from home.models import Informacion, Image, Video


class InformacionAdmin(admin.ModelAdmin):
    list_display = ('titulo',)


class MediaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'calificacion')
    ordering = ('-calificacion',)


admin.site.register(Informacion, InformacionAdmin)
admin.site.register(Image, MediaAdmin)
admin.site.register(Video, MediaAdmin)
