# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-10 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_exam_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='file',
            field=models.FileField(upload_to='uploads'),
        ),
    ]
