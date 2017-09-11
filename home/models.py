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
    titulo_extra = models.CharField(max_length=250, blank=True)
    texto_extra = models.TextField(max_length=2000, blank=True)
    
    def __str__(self):
        return 'Información de ' + self.titulo
      
    class Meta:
        verbose_name = 'Información'
        verbose_name_plural = 'Información'


class Image(models.Model):
    nombre = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    calificacion = models.IntegerField(validators=[MinValueValidator(1),
                                                   MaxValueValidator(5)])
    
    def __str__(self):
        return 'Objeto de imágen ' + self.nombre
      
    class Meta:
        verbose_name = 'Imágen'
        verbose_name_plural = 'Imágenes'


class Video(models.Model):
    nombre = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    calificacion = models.IntegerField(validators=[MinValueValidator(1),
                                                   MaxValueValidator(5)])
    
    def __str__(self):
        return 'Objeto de video ' + self.nombre
      
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
