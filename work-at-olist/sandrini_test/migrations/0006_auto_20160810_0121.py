# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandrini_test', '0005_auto_20160809_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]