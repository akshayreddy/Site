# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 08:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170720_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='url',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
