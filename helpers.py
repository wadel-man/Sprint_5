import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators, MainPageLocators
from data import USER_EMAIL, USER_PASSWORD



login = 'ravil_askyanov_58'

def generate_login():
    generate_login_int = random.randint(100,999)
    return f'{login}_{generate_login_int}@yandex.ru'


def generate_password():
    password = random.randint(100000,999999)
    return f'{password}'


def helper_func_with_valid_data(driver):
        driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(USER_EMAIL)
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BTN))