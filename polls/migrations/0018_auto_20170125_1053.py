# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-25 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20170125_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='battery',
        ),
        migrations.AddField(
            model_name='service',
            name='Battery: good/ok/bad',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
