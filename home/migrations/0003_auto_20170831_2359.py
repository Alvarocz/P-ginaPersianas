# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170831_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacion',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='texto_mision',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='texto_servicios',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='texto_vision',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='titulo_mision',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='titulo_servicios',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='titulo_vision',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]