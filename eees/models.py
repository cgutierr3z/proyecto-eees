# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
import datetime

#Modelo Departametos
class Departamento(models.Model):
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    departamento    = models.CharField(max_length=200)

    def __str__(self):
        return self.departamento

#Modelo Municipios
class Municipio(models.Model):
    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

    departamento    = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio       = models.CharField(max_length=200)

    def __str__(self):
        return self.municipio
