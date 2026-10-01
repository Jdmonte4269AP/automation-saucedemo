import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    wait = WebDriverWait(driver,10)

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = wait.until(EC.presence_of_element_located((By.ID,"user-name")))
        #driver.find_element(By.ID,"user-name")
        password = wait.until(EC.presence_of_element_located((By.ID,"password")))
        #driver.find_element(By.ID,"password")
        
        boton_login = wait.until(EC.element_to_be_clickable((By.ID,"login-button")))
        
        # driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        boton_login.click()

        assert "/inventory.html" in driver.current_url

        # Validacion texto
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        titulo = driver.find_element(By.CSS_SELECTOR,"[data-test='title']")
        assert titulo.text == "Products"
    finally:
        driver.quit()
