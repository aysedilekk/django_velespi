# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name_plural': 'Media'},
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(upload_to=b'places'),
        ),
    ]
