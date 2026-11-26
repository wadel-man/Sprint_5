from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, RecoveryPasswordPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import USER_EMAIL, USER_PASSWORD
from helpers import helper_func_with_valid_data


class TestLogin:


    def test_login_main_page_button_successful(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
        helper_func_with_valid_data(driver)
    
        assert driver.find_element(*MainPageLocators.ORDER_BTN).is_displayed()

    def test_personal_account_button_successful(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
        helper_func_with_valid_data(driver)

        assert driver.find_element(*MainPageLocators.ORDER_BTN).is_displayed()

    def test_login_registration_form_button_successful(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
        driver.find_element(*LoginPageLocators.BTN_REGISTRATION).click()
        driver.find_element(*RegistrationPageLocators.RGR_LOGIN).click()
        helper_func_with_valid_data(driver)

        assert driver.find_element(*MainPageLocators.ORDER_BTN).is_displayed()

    def test_login_recovery_form_button_successful(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
        driver.find_element(*LoginPageLocators.RE_PASSWORD_BTN).click()
        driver.find_element(*RecoveryPasswordPageLocators.LOGIN_BTN).click()
        helper_func_with_valid_data(driver)

        assert driver.find_element(*MainPageLocators.ORDER_BTN).is_displayed()



