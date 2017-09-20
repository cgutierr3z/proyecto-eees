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

    departamento    = models.CharField(max_length=200, unique=True, null=False)
    is_active       = models.BooleanField('Activo', default=True)


    def __str__(self):
        return self.departamento

    def desactivar(self):
        self.is_active = False

    def activar(self):
        self.is_active = True

#Modelo Municipios
class Municipio(models.Model):
    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

    departamento    = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio       = models.CharField(max_length=200,unique=True, null=False)
    is_active       = models.BooleanField('Activo', default=True)

    def __str__(self):
        return str(self.departamento) +str(' - ')+ str(self.municipio)

    def desactivar(self):
        self.is_active = False
        return self

    def activar(self):
        self.is_active = True
        return self

#Modelo de Colegio
class Colegio(models.Model):
    class Meta:
        verbose_name = "Colegio"
        verbose_name_plural = "Colegios"

    nombre          = models.CharField(max_length=200,  unique=True, null=False)
    municipio       = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    is_active       = models.BooleanField('Activar', default=True)

    def __str__(self):
        return str(self.municipio) +str(' - ')+ str(self.nombre)

    def desactivar(self):
        self.is_active = False

    def activar(self):
        self.is_active = True

#Modelo de usuarios
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
    manejodatos         = models.BooleanField('Manejo datos',default=False)

    def desactivar(self):
        self.is_active = False

    def activar(self):
        self.is_active = True

class Administrador(Usuario):
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

    departamento        = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True, blank=True)
    municipio           = models.ForeignKey(Municipio, on_delete=models.PROTECT, null=True, blank=True)


class Profesor(Usuario):
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    departamento        = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True, blank=True)
    municipio           = models.ForeignKey(Municipio, on_delete=models.PROTECT, null=True, blank=True)


#Modelo de grupos
class Grupo(models.Model):
    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    JORNADA_LIST = [
        ('MANANA', 'MANANA'),
        ('TARDE', 'TARDE'),
        ('UNICA', 'UNICA'),
        ('NOCTURNA', 'NOCTURNA'),
        ('SABATINA', 'SABATINA'),
    ]
    GRADOS_LIST = [
        ('PRIMARIA',(
                ('0','CERO'),
                ('1','PRIMERO'),
                ('2','SEGUNDO'),
                ('3','TERCERO'),
                ('4','CUARTO'),
                ('5','QUINTO'),
            )
        ),
        ('SECUNDARIA',(
                ('6','SEXTO'),
                ('7','SEPTIMO'),
                ('8','OCTAVO'),
                ('9','NOVENO'),
                ('10','DECIMO'),
                ('11','UNDECIMO'),
            )
        ),
    ]
    colegio     = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    jornada     = models.CharField(max_length=200,choices=JORNADA_LIST)
    grado       = models.CharField(max_length=200,choices=GRADOS_LIST)
    nombre      = models.CharField(max_length=200)
    profesor    = models.ForeignKey(Profesor, on_delete=models.PROTECT, null=True, blank=True)
    is_active   = models.BooleanField('Activar',default=True)


    def __str__(self):
        return str(self.colegio) +str(' - ')+ str(self.nombre)

    def desactivar(self):
        self.is_active = False

    def activar(self):
        self.is_active = True

class Estudiante(Usuario):
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    #user        = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    #active      = models.BooleanField(default=True)
    departamento        = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True, blank=True)
    municipio           = models.ForeignKey(Municipio, on_delete=models.PROTECT, null=True, blank=True)
    grupo               = models.ForeignKey(Grupo, on_delete=models.CASCADE)
