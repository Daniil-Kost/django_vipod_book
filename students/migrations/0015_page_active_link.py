# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-26 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_auto_20180324_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='active_link',
            field=models.BooleanField(default=False),
        ),
    ]
