from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart():
    driver = webdriver.Chrome()
    
    wait = WebDriverWait(driver,10)

    try:
        # Login
        driver.get("https://www.saucedemo.com/")
        
        wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        password.send_keys("secret_sauce")

        boton_login.click()
        
        primer_producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_item")))
        
        nombre_producto = primer_producto.find_element(By.CLASS_NAME,"inventory_item_name").text
        boton_agregar = primer_producto.find_element(By.TAG_NAME,"button")
        
        boton_agregar.click()
        
        contador_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        
        assert contador_carrito.text == "1"
        
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link"))).click()
        
        nombre_producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_item_name"))).text
        
        assert nombre_producto == nombre_producto_carrito
        
    finally:
            driver.quit()