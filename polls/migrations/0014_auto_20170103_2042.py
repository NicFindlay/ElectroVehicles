# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_service_technician'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_pic_one',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart_pic_three',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart_pic_two',
        ),
    ]
