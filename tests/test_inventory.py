from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

def test_inventory(driver):
    try:
        logger.info("Inicializando la prueba de Inventario")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        logger.info("Ingresando a la pagina web")
        driver.get("https://www.saucedemo.com/")
        
        logger.info("Ingresando credenciales para iniciar sesion")
        login_page.login("standard_user","secret_sauce")
        logger.info("Sesion iniciada correctamente")
        
        productos = inventory_page.obtener_productos()
        logger.info("Productos de la pagina web capturados")

        assert len(productos) > 0
        logger.info("Prueba de cantidad de productos validada")
        
        assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
        assert inventory_page.obtener_precio_primer_producto() == "$29.99"
        logger.info("Prueba de integradad de la informacion de los productos validada")
        
        assert inventory_page.menu_visible()
        logger.info("Prueba de visibilidad del menu en la pagina validada")
        
        assert inventory_page.filtro_visible()
        logger.info("Prueba de visibilidad del filtro en la pagina validada")
    except Exception:
        logger.exception("Error durante la prueba de Inventario")
        raise