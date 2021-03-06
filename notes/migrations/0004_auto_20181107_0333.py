# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-07 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20181107_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
