# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 16:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opm_app', '0005_auto_20170412_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='father_name',
        ),
    ]
