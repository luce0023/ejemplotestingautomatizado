# base_test.py
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class BaseTest(unittest.TestCase):
    """Clase base que contiene la configuración común (setup/teardown) para todos los tests."""
    
    def setUp(self):
        # NOTA: En un proyecto real, necesitarías tener ChromeDriver instalado y configurado.
        # Aquí inicializamos el driver (puede requerir ajustes locales)
        self.driver = webdriver.Chrome() 
        self.driver.implicitly_wait(10) 
        self.base_url = "https://www.saucedemo.com/"
        self.driver.get(self.base_url)
    
    def tearDown(self):
        # self.driver.quit() # Descomentar para cerrar el navegador en local
        pass # Dejar pass si no se puede ejecutar en tu laptop

    def login_standard_user(self):
        """Método de ayuda para iniciar sesión en los tests que lo requieran."""
        from pages.login_page import LoginPage
        login_page = LoginPage(self.driver)
        login_page.enter_credentials("standard_user", "secret_sauce")
        login_page.click_login()