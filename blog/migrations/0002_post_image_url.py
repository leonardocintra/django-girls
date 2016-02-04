# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 02:14
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='produto-sem-imagem'),
        ),
    ]
