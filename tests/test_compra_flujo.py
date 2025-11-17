# tests/test_compra_flujo.py
import unittest
from base_test import BaseTest
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCompraFlujo(BaseTest):
    
    def setUp(self):
        super().setUp()
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        # Inicio de sesión automático para estos tests, usando el método base
        self.login_standard_user()

    def test_01_compra_completa_exitosa(self):
        """Refactor de ComprarProductosSeleccionados.py: Flujo completo de compra."""
        
        # 1. Seleccionar productos (usando la lógica de products_page)
        self.products_page.add_product_by_id("backpack")
        
        # 2. Ir al carrito e iniciar checkout
        self.products_page.go_to_cart()
        self.cart_page.click_checkout()
        
        # 3. Llenar información (usando la lógica de checkout_page)
        self.checkout_page.fill_user_info("abcde", "abcde", "15304")
        self.checkout_page.click_continue()
        
        # 4. Finalizar
        self.checkout_page.click_finish()
        
        # VERIFICACIÓN SENIOR
        self.assertTrue(self.driver.current_url.endswith("checkout-complete.html"), "ERROR: La compra no se finalizó exitosamente.")

    def test_02_cancelar_compra(self):
        """Refactor de CancelarCompraDeProductosSeleccionados.py: Flujo de compra cancelado."""

        # 1. Seleccionar producto (usando la lógica de products_page)
        self.products_page.add_product_by_id("bolt-t-shirt")
        
        # 2. Ir al carrito e iniciar checkout
        self.products_page.go_to_cart()
        self.cart_page.click_checkout()
        
        # 3. Llenar información
        self.checkout_page.fill_user_info("abcde", "abcde", "12543")
        self.checkout_page.click_continue()
        
        # 4. Cancelar
        self.checkout_page.click_cancel()
        
        # VERIFICACIÓN SENIOR: Debe volver a la página de productos (inventory)
        self.assertTrue(self.driver.current_url.endswith("inventory.html"), "ERROR: La cancelación no regresó a la página de productos.")

    def test_03_quitar_productos_del_carrito(self):
        """Refactor de QuitarProductosDeCarritoDeCompras.py: Añadir y quitar productos."""
        
        # 1. Seleccionar productos
        self.products_page.add_product_by_id("backpack")
        self.products_page.add_product_by_id("bike-light")
        
        # 2. Ir al carrito (Ahora debe haber 2 ítems)
        self.products_page.go_to_cart()
        self.assertEqual(self.cart_page.get_item_count(), 2, "ERROR: Inicialmente, debe haber 2 productos en el carrito.")

        # 3. Quitar la mochila
        self.cart_page.click_remove_backpack()
        
        # VERIFICACIÓN SENIOR: Debe quedar 1 ítem
        self.assertEqual(self.cart_page.get_item_count(), 1, "ERROR: Solo debe quedar 1 producto en el carrito después de quitar uno.")