# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departamento',
            old_name='departamento',
            new_name='departamento_txt',
        ),
        migrations.RenameField(
            model_name='municipio',
            old_name='municipio',
            new_name='municipio_txt',
        ),
    ]