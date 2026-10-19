from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

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
       
    def agregar_producto(self,nombre):
        productos = self.obtener_productos()
        for producto in productos:
            nombre_producto = producto.find_element(By.CLASS_NAME,"inventory_item_name").text
            if nombre_producto == nombre:
                print(nombre_producto)
                producto.find_element(By.TAG_NAME,"button").click()
                return
            
        raise AssertionError(f"No se encontró el producto: {nombre}")
    
    def obtener_contador_carrito(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge"))).text

    def ir_al_carrito(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link"))).click()
