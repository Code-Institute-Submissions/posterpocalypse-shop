# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-07 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200507_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='image',
        ),
    ]