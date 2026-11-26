import pytest
from data import BASE_URL
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()

    browser.get(BASE_URL)

    yield browser


    browser.quit()