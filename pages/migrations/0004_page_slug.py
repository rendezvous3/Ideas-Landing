# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-16 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20170315_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='page-slug'),
        ),
    ]
