from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

    def obtener_productos(self):
        return self.driver.find_elements(By.CLASS_NAME,"inventory_item")

    def obtener_nombre_primer_producto(self):
        producto = self.obtener_productos()

        return producto[0].find_element(By.CLASS_NAME,"inventory_item_name").text

    def obtener_precio_primer_producto(self):
            producto = self.obtener_productos()
    
            return producto[0].find_element(By.CLASS_NAME,"inventory_item_price").text

    def menu_visible(self):
       menu = self.driver.find_element(By.ID,"react-burger-menu-btn")

       return menu.is_displayed() 

    def filtro_visible(self):
           filtro = self.driver.find_element(By.ID,"product_sort_container")
    
           return filtro.is_displayed() 