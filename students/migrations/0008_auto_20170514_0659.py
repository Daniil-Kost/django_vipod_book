# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-14 06:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20170514_0655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='group',
            new_name='groups',
        ),
    ]
