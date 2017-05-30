# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0002_author_book_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]