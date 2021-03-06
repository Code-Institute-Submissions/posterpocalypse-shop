# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-23 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('Movie Posters', 'Movie Posters'), ('Music TV Posters', 'Music TV Posters'), ('Art Prints', 'Art Prints')], max_length=250)),
                ('description', models.TextField()),
                ('artist', models.CharField(default='', max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
