import pytest

from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()

    browser.get('https://stellarburgers.education-services.ru/')

    yield browser


    browser.quit()