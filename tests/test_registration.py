from data import generate_login, generate_password
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_successful(driver):

    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
    driver.find_element(*LoginPageLocators.BTN_REGISTRATION).click()
    driver.find_element(*RegistrationPageLocators.RGR_NAME).send_keys('Равиль')
    driver.find_element(*RegistrationPageLocators.RGR_EMAIL).send_keys(generate_login())
    driver.find_element(*RegistrationPageLocators.RGR_PASS).send_keys(generate_password())
    driver.find_element(*RegistrationPageLocators.RGR_BTN).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BTN))

    assert driver.find_element(*LoginPageLocators.LOGIN_BTN).is_displayed()
 

    


def test_registration_incorrect_password_error(driver):
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
    driver.find_element(*LoginPageLocators.BTN_REGISTRATION).click()
    driver.find_element(*RegistrationPageLocators.RGR_NAME).send_keys('Равиль')
    driver.find_element(*RegistrationPageLocators.RGR_EMAIL).send_keys(generate_login())
    driver.find_element(*RegistrationPageLocators.RGR_PASS).send_keys('12345')
    driver.find_element(*RegistrationPageLocators.RGR_BTN).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.ERROR_PASS_TEXT))

    assert driver.find_element(*RegistrationPageLocators.ERROR_PASS_TEXT).text == 'Некорректный пароль'



