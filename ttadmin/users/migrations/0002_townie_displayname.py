# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='townie',
            name='displayname',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]