# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 07:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 1, 7, 25, 10, 314000, tzinfo=utc)),
        ),
    ]
