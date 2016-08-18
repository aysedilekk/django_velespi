# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-18 08:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0003_auto_20160816_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='likes',
            field=models.ManyToManyField(related_name='liked_places', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinates',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_places', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='vote',
            field=models.IntegerField(choices=[(1, 'Berbat'), (2, 'Kötü'), (3, 'Meh'), (4, 'Uh'), (5, 'Yıkılıyor')], default=3),
        ),
    ]
