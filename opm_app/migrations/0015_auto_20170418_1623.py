# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opm_app', '0014_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
