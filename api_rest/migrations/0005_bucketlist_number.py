# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-20 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0004_auto_20170719_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='number',
            field=models.FloatField(default=''),
        ),
    ]
