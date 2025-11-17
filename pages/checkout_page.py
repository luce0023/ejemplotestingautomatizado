# pages/checkout_page.py
from selenium.webdriver.common.by import By

class CheckoutPage:
    # LOCALIZADORES - Step One (Información)
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    
    # LOCALIZADORES - Step Two (Overview/Resumen)
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    def __init__(self, driver):
        self.driver = driver

    def fill_user_info(self, first_name, last_name, postal_code):
        """Llena los campos de información de envío."""
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(postal_code)
    
    def click_continue(self):
        """Avanza al resumen de la compra."""
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        
    def click_finish(self):
        """Finaliza la compra."""
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def click_cancel(self):
        """Cancela el proceso de compra."""
        self.driver.find_element(*self.CANCEL_BUTTON).click()