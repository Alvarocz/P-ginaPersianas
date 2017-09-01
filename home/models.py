from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Informacion(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=90, blank=True)
    titulo_servicios = models.CharField(max_length=250, blank=True)
    texto_servicios = models.TextField(max_length=2000, blank=True)
    titulo_mision = models.CharField(max_length=250, blank=True)
    texto_mision = models.TextField(max_length=2000, blank=True)
    titulo_vision = models.CharField(max_length=250, blank=True)
    texto_vision = models.TextField(max_length=2000, blank=True)


class Image(models.Model):
    nombre = models.CharField(max_length=20)
    url = models.CharField(max_length=150)
    calificacion = models.IntegerField(validators=[MinValueValidator(1),
                                                   MaxValueValidator(5)])
