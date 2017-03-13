# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-13 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='layout',
            field=models.CharField(choices=[('standard', 'Standard'), ('stacked', 'Stacked')], default='standard', max_length=20),
        ),
        migrations.AddField(
            model_name='page',
            name='nav_color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AddField(
            model_name='page',
            name='show_nav',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='page',
            name='video_embed',
            field=models.TextField(blank=True, null=True),
        ),
    ]