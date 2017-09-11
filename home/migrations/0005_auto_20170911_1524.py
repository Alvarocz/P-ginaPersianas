# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 15:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170908_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=150)),
                ('calificacion', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Imágen', 'verbose_name_plural': 'Imágenes'},
        ),
        migrations.AlterModelOptions(
            name='informacion',
            options={'verbose_name': 'Información', 'verbose_name_plural': 'Información'},
        ),
    ]
