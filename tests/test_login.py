from pages.login_page import LoginPage
import pytest
from utils.reader import read_users_csv

@pytest.mark.parametrize(
        "data",read_users_csv())
def test_login(driver,data):
    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com/")

    login_page.login(data["usuario"],data["password"])

    if (data["tipo_usuario"] == "True"):
        assert "/inventory.html" in driver.current_url
    elif data["tipo_usuario"] == "False":
        error = login_page.obtener_mensaje_error()
        print(error)
        assert "Epic sadface" in error