import pytest
from selenium import webdriver

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

