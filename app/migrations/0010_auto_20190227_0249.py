# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190227_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newform',
            name='ArrivalDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='my date'),
        ),
        migrations.AlterField(
            model_name='newform',
            name='DepatureDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='my date'),
        ),
    ]