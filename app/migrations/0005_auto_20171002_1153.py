# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170929_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securitybond',
            name='ratelist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='ratelist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='ratelist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='ratelist',
            field=models.IntegerField(),
        ),
    ]
