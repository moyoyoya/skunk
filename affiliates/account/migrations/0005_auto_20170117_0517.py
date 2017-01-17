# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20170117_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='relationship',
        ),
        migrations.AddField(
            model_name='profile',
            name='active_arg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='active_chl',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='active_col',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='active_mex',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='active_pan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='active_per',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='active_ven',
            field=models.BooleanField(default=False),
        ),
    ]