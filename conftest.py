import pytest
from selenium import webdriver

import pytest_html
import pathlib
import base64

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)


    yield driver

    driver.quit()
    
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return { "x-api-key": "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        carpeta = pathlib.Path("reports/screenshots")
        carpeta.mkdir(parents=True,exist_ok=True)
        archivo = carpeta / f"{item.name}.png"

        driver.save_screenshot(str(archivo))

        imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")
        report.extras = [
            pytest_html.extras.png(imagen, name="Screenshot")
        ]
