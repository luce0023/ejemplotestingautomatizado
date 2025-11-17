# tests/test_login.py
import unittest
from base_test import BaseTest
from pages.login_page import LoginPage

class TestLogin(BaseTest):
    
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)

    def test_01_login_correcto(self):
        """Verifica que un usuario estándar pueda iniciar sesión exitosamente."""
        
        self.login_page.enter_credentials("standard_user", "secret_sauce")
        self.login_page.click_login()
        
        # VERIFICACIÓN SENIOR: Asegurarse de que el URL finalice en /inventory.html
        current_url = self.driver.current_url
        self.assertTrue(current_url.endswith("inventory.html"), "ERROR: Login correcto no navegó a la página de productos.")
    
    def test_02_login_incorrecto_credenciales(self):
        """Verifica que el login falle con credenciales inválidas (simulando locked_out_user y error de contraseña)."""
        
        self.login_page.enter_credentials("locked_out_user", "secreat_sauce") # El error de ortografía 'secreat' está en tu original
        self.login_page.click_login()
        
        # VERIFICACIÓN SENIOR: Asegurarse de que el mensaje de error es el esperado
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        actual_error = self.login_page.get_error_message()
        
        self.assertEqual(actual_error, expected_error, "ERROR: El mensaje de error no coincide.")