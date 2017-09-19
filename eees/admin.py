# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Colegio)
admin.site.register(Grupo)
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Profesor)
admin.site.register(Estudiante)
