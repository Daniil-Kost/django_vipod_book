# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-10 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stud_auth', '0003_stprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='stprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='stprofile',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='stprofile',
            name='username',
        ),
    ]