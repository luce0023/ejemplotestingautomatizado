# pages/cart_page.py
from selenium.webdriver.common.by import By

class CartPage:
    # LOCALIZADORES
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    def __init__(self, driver):
        self.driver = driver
        
    def click_remove_backpack(self):
        """Quita la mochila del carrito."""
        self.driver.find_element(*self.REMOVE_BACKPACK_BUTTON).click()

    def click_checkout(self):
        """Inicia el proceso de checkout."""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        
    def get_item_count(self):
        """Cuenta cuántos items hay en el carrito."""
        return len(self.driver.find_elements(*self.CART_ITEM))