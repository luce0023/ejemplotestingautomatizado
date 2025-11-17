# pages/products_page.py
from selenium.webdriver.common.by import By

class ProductsPage:
    # LOCALIZADORES
    SHOPPING_CART_LINK = (By.XPATH, "//div[@id='shopping_cart_container']/a")
    # Los localizadores de productos se generan dinámicamente

    def __init__(self, driver):
        self.driver = driver

    def add_product_by_id(self, product_id):
        """Añade un producto al carrito usando su ID específico (ej: 'backpack')."""
        self.driver.find_element(By.ID, f"add-to-cart-sauce-labs-{product_id}").click()

    def go_to_cart(self):
        """Navega al carrito de compras."""
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()