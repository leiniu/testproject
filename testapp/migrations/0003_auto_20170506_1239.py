# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 04:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20170506_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='prd_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Prd'),
        ),
    ]
