# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-06 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170516_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_HT',
            field=models.IntegerField(verbose_name='prix public HT'),
        ),
    ]