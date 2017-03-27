# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-19 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0003_auto_20170316_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='turnout',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gmina',
            name='turnout',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='powiat',
            name='turnout',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wojewodztwo',
            name='turnout',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
    ]