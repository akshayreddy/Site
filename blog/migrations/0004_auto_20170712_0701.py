# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_profileinfo_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='thumbnail',
            field=models.FileField(blank=True, upload_to='profile_image'),
        ),
    ]