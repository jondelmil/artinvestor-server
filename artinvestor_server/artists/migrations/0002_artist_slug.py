# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(default='unknown', unique=True),
            preserve_default=False,
        ),
    ]
