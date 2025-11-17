# Proyecto de Automatización QA - Sauce Demo

## Introducción
Este proyecto demuestra la implementación de pruebas de automatización web utilizando **Python** y **Selenium WebDriver** bajo el patrón de diseño **Page Object Model (POM)**. Los casos de prueba están enfocados en la aplicación de demostración [Sauce Demo](https://www.saucedemo.com/).

## Estructura del Proyecto (POM)
* **`/pages`**: Contiene los Page Objects (modelos de las páginas web) con todos los localizadores y métodos de interacción. Esto garantiza la **mantenibilidad**.
* **`/tests`**: Contiene los escenarios de prueba (qué se prueba) que utilizan las clases de `/pages`.
* **`base_test.py`**: Clase base para la configuración del `WebDriver` (Setup y Teardown).

## Requisitos
Para ejecutar estas pruebas, necesitarás:
1.  Python 3.x
2.  Selenium WebDriver
3.  El Driver del navegador (ej. Chrome, Firefox) en tu PATH.

## Instalación
1.  Clonar este repositorio.
2.  Instalar las dependencias (ver `requirements.txt`).
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución
```bash
python -m unittest tests.test_login
# O para ejecutar todos los tests:
python -m unittest discover tests
