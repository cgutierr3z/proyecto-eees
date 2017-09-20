# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import *

# Create your tests here.

class DepartamentoTest(TestCase):
    def setUp(self):
        self.depto1, self.create1 = Departamento.objects.get_or_create(departamento='Risaralda')
        self.depto2, self.create2 = Departamento.objects.get_or_create(departamento='Risaralda')

    def test_create_departamento(self):
        self.assertIsInstance(self.depto1, Departamento)

    def test_create_departamento_duplicado(self):
        self.assertTrue(self.create1)
        self.assertFalse(self.create2)

    def test_create_departamento_is_active(self):
        self.assertTrue(self.depto1.is_active)

    def test_departamento_desactivar(self):
        self.depto1.desactivar()
        self.assertFalse(self.depto1.is_active)

    def test_departamento_activar(self):
        self.depto1.desactivar()
        self.depto1.activar()
        self.assertTrue(self.depto1.is_active)

class MunicipioTest(TestCase):
    def setUp(self):
        self.depto, self.create = Departamento.objects.get_or_create(departamento='Risaralda')
        self.munpi1, self.create1 = Municipio.objects.get_or_create(departamento=self.depto, municipio='Pereira')
        self.munpi2, self.create2 = Municipio.objects.get_or_create(departamento=self.depto, municipio='Pereira')

    def test_create_colegio(self):
        self.assertIsInstance(self.munpi1, Municipio)

    def test_create_colegio_duplicado(self):
        self.assertTrue(self.create1)
        self.assertFalse(self.create2)

    def test_create_colegio_is_active(self):
        self.assertTrue(self.munpi1.is_active)

    def test_colegio_desactivar(self):
        self.munpi1.desactivar()
        self.assertFalse(self.munpi1.is_active)

    def test_colegio_activar(self):
        self.munpi1.desactivar()
        self.munpi1.activar()
        self.assertTrue(self.munpi1.is_active)

class ColegioTest(TestCase):
    def setUp(self):
        self.depto, self.c1 = Departamento.objects.get_or_create(departamento='Risaralda')
        self.munpi, self.c2 = Municipio.objects.get_or_create(departamento=self.depto, municipio='Pereira')
        self.col1, self.create1 = Colegio.objects.get_or_create(municipio=self.munpi, nombre='INEM')
        self.col2, self.create2 = Colegio.objects.get_or_create(municipio=self.munpi, nombre='INEM')

    def test_create_colegio(self):
        self.assertIsInstance(self.col1, Colegio)

    def test_create_colegio_duplicado(self):
        self.assertTrue(self.create1)
        self.assertFalse(self.create2)

    def test_create_colegio_is_active(self):
        self.assertTrue(self.col1.is_active)

    def test_colegio_desactivar(self):
        self.col1.desactivar()
        self.assertFalse(self.col1.is_active)

    def test_colegio_activar(self):
        self.col1.desactivar()
        self.col1.activar()
        self.assertTrue(self.col1.is_active)
