# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-14 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manago', '0005_auto_20170306_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
