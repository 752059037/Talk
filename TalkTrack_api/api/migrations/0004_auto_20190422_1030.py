# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-22 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190422_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceconfig',
            name='record_start',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deviceconfig',
            name='work_time_end',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deviceconfig',
            name='work_time_start',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
