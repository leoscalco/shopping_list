# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.AddField(
            model_name='instanceditem',
            name='price_unit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]