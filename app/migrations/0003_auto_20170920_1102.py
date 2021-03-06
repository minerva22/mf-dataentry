# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170920_1029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ('name', 'code_leb', 'code_dub'), 'verbose_name_plural': 'currencies'},
        ),
        migrations.AlterModelOptions(
            name='nationality',
            options={'ordering': ('name', 'code_leb', 'code_dub'), 'verbose_name_plural': 'nationalities'},
        ),
        migrations.AlterField(
            model_name='currency',
            name='code_dub',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='code_leb',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='nationality',
            name='code_dub',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='nationality',
            name='code_leb',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
