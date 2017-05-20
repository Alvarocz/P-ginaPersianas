from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Image(models.Model):
    nombre = models.CharField(max_length=20)
    url = models.CharField(max_length=150)
    calificacion = models.IntegerField(validators=[MinValueValidator(1),
                                                   MaxValueValidator(5)])
