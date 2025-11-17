# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class QuitarProductosDeCarritoDeCompras(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_quitar_productos_de_carrito_de_compras(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element_by_id("user-name").clear()
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()
        driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
        driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
        driver.find_element_by_xpath("//div[@id='shopping_cart_container']/a/span").click()
        driver.find_element_by_id("remove-sauce-labs-backpack").click()
        driver.find_element_by_id("continue-shopping").click()
        driver.find_element_by_id("remove-sauce-labs-bike-light").click()
        driver.find_element_by_xpath("//div[@id='shopping_cart_container']/a").click()
        driver.find_element_by_id("continue-shopping").click()
        driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
