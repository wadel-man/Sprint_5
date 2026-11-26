from locators import MainPageLocators

def test_navigate_to_sauce_section_successful(driver):
    driver.find_element(*MainPageLocators.SAUCE_BTN).click()

    assert driver.find_element(*MainPageLocators.ACTIVE_TAB).text == 'Соусы'

def test_navigate_to_buns_section_successful(driver):
    driver.find_element(*MainPageLocators.SAUCE_BTN).click()

    driver.find_element(*MainPageLocators.BUNS_BTN).click()
    assert driver.find_element(*MainPageLocators.ACTIVE_TAB).text == 'Булки'

def test_navigate_to_fillings_section_successful(driver):
    driver.find_element(*MainPageLocators.FILLINGS_BTN).click()

    assert driver.find_element(*MainPageLocators.ACTIVE_TAB).text == 'Начинки'