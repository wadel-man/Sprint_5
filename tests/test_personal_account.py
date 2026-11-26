from locators import MainPageLocators, LoginPageLocators,  ProfilePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import USER_EMAIL, USER_PASSWORD
from tests.test_login import helper_func_with_valid_data


def test_go_to_personal_account_button_successful(driver):
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
    helper_func_with_valid_data(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGOUT_BTN))

    assert driver.find_element(*ProfilePageLocators.LOGOUT_BTN).is_displayed()

def test_from_personal_acc_to_the_constructor_btn_successful(driver):
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
    helper_func_with_valid_data(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
    driver.find_element(*MainPageLocators.CONSTRUCTOR_BTN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BTN))

    assert driver.find_element(*MainPageLocators.ORDER_BTN).is_displayed()

def test_from_personal_account_to_the_logo_successful(driver):
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
    helper_func_with_valid_data(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
    driver.find_element(*MainPageLocators.LOGO).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BTN))

    assert driver.find_element(*MainPageLocators.ORDER_BTN).is_displayed()


def test_logout_of_personal_account_btn_successful(driver):
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
    helper_func_with_valid_data(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGOUT_BTN))
    driver.find_element(*ProfilePageLocators.LOGOUT_BTN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.RE_PASSWORD_BTN))

    assert driver.find_element(*LoginPageLocators.RE_PASSWORD_BTN).is_displayed()


    
    


