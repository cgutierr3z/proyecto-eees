# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eees', '0006_auto_20170918_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='eees.Departamento'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='eees.Municipio'),
        ),
    ]
