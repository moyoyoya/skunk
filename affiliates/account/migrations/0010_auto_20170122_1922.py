# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20170119_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='ad_space',
            field=models.IntegerField(unique=True),
        ),
    ]
