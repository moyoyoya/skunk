# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20170117_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='affiliate_id',
            field=models.IntegerField(null=True),
        ),
    ]
