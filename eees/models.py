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
        return str(self.departamento) +str(' - ')+ str(self.municipio)

#Modelo de Colegio
class Colegio(models.Model):
    class Meta:
        verbose_name = "Colegio"
        verbose_name_plural = "Colegios"

    nombre          = models.CharField(max_length=200)
    departamento    = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio       = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    is_active       = models.BooleanField('Activar', default=True)

    def __str__(self):
        return self.nombre

    def desactivar(self):
        self.is_active = False

    def activar(self):
        self.is_active = True

#modelo de usuarios
class Usuario(AbstractUser):
    class Meta:
        db_table = 'auth_user'
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    TIPO_DOC_LIST = [
        ('CEDULA CUIDADANIA', 'CEDULA CUIDADANIA'),
        ('CEDULA EXTRANJERIA', 'CEDULA EXTRANJERIA'),
        ('PASAPORTE', 'PASAPORTE'),
        ('TARJETA IDENTIDAD', 'TARJETA IDENTIDAD'),
    ]
    GENERO_LIST= [
        ('HETEROSEXUAL', 'HETEROSEXUAL'),
        ('HOMOSEXUAL', 'HOMOSEXUAL'),
        ('LESBIANA', 'LESBIANA'),
        ('BISEXUAL', 'BISEXUAL'),
        ('INDIFERENCIADO', 'INDIFERENCIADO'),
    ]

    is_admin            = models.BooleanField('Administrador',default=False)
    is_profe            = models.BooleanField('Profesor',default=False)
    is_estud            = models.BooleanField('Estudiante',default=False)
    tipo_docto          = models.CharField('Tipo documento',max_length=20,choices=TIPO_DOC_LIST)
    no_docto            = models.CharField('Numero documento',max_length=20)
    fecha_nac           = models.DateField('Fecha nacimiento',null=True)
    genero              = models.CharField('Genero',max_length=20,choices=GENERO_LIST)
    direccion           = models.CharField('Direccion',max_length=100)
    telefono            = models.CharField('Telefono',max_length=15)

    def desactivar(self):
        self.is_active = False

    def activar(self):
        self.is_active = True
