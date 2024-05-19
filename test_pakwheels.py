import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.pakwheels.com/")
    yield driver
    driver.quit()

def test_home_page_title(setup):
    assert "New Cars, Used Cars, Bikes Prices, News, Reviews | PakWheels" in setup.title

def test_search_function(setup):
    search_box = setup.find_element(By.NAME, "q")
    search_box.send_keys("Toyota")
    search_box.submit()
    results = setup.find_elements(By.CLASS_NAME, "search-result")
    assert len(results) > 0
