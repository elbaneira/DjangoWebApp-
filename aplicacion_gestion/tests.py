from django.test import TestCase
from django.urls import reverse

class ProyectoSmokeTest(TestCase):
    def test_pagina_inicio_responde_ok(self):
        """Valida que la página principal o de login cargue correctamente (Código HTTP 200)"""
        #  url de login 
        url = reverse('login') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_creacion_objeto_basico(self):
        """Valida una condición lógica básica"""
        self.assertEqual(1 + 1, 2)
