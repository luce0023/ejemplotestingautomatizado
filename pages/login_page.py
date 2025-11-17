# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    # 1. LOCALIZADORES (Definición de elementos)
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    def __init__(self, driver):
        self.driver = driver

    # 2. MÉTODOS DE ACCIÓN (Operaciones sobre los elementos)
    def enter_credentials(self, username, password):
        """Escribe usuario y contraseña en los campos correspondientes."""
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
    
    def click_login(self):
        """Hace clic en el botón de Login."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        
    def get_error_message(self):
        """Retorna el texto del mensaje de error."""
        return self.driver.find_element(*self.ERROR_MESSAGE).text
