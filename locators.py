from selenium.webdriver.common.by import By

class MainPageLocators:

     
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//button[text()='Войти в аккаунт']") #кнопка Войти в аккаунт
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//a[@href='/account']") #кнопка Личный кабинет
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[text()='Конструктор']") # кнопка Конструктор
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a") # логотип
    BUNS_BTN = (By.XPATH, "//span[text()='Булки']") # кнопка булки
    SAUCE_BTN = (By.XPATH, "//span[text()='Соусы']") # кнопка соусы
    FILLINGS_BTN = (By.XPATH, "//span[text()='Начинки']") # кнопка начинки
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") # подчёркивание у активной кнопки
    ORDER_BTN = (By.XPATH, "//div//button[text()='Оформить заказ']") # кнопка оформления заказа на главной странице когда авторизирован


class LoginPageLocators:
    INPUT_EMAIL = (By.XPATH, "//div//label[text()='Email']/../input") # Поле ввода Email
    INPUT_PASSWORD = (By.XPATH, "//div//label[text()='Пароль']/../input") # Поле ввода пароля
    LOGIN_BTN = (By.XPATH, "//form//button[text()='Войти']") # Кнопка Войти в окне входа
    BTN_REGISTRATION = (By.XPATH, "//div//a[@href='/register']")# Кнопка Зарегистрироваться в окне входа
    RE_PASSWORD_BTN = (By.XPATH, "//div//a[@href='/forgot-password']") # Кнопка Восстановить пароль 


class RegistrationPageLocators:
    RGR_NAME = (By.XPATH, "//div//label[text()='Имя']/../input") # Поле Имя
    RGR_EMAIL = (By.XPATH, "//div//label[text()='Email']/../input") # Поле Email
    RGR_PASS = (By.XPATH, "//div//label[text()='Пароль']/../input") # Поле Пароль
    RGR_BTN = (By.XPATH, "//div//button[text()='Зарегистрироваться']") # Кнопка Зарегистрироваться
    RGR_LOGIN = (By.XPATH, "//div//a[@href='/login']") # Кнопка войти в окне регистрации
    ERROR_PASS_TEXT = (By.XPATH, "//div//p[text()='Некорректный пароль']") # Некорректный пароль


class RecoveryPasswordPageLocators:
    EMAIL_BTN = (By.XPATH, "//div//label[text()='Email']/../input") # Кнопка Email в окне восстановления пароля
    RESTORE_BTN = (By.XPATH, "//div//button[text()='Восстановить']") # Кнопка Восстановить
    LOGIN_BTN = (By.XPATH, "//div//a[@href='/login']") # кнопка войти в окне восстановления пароля


class ProfilePageLocators:
    LOGOUT_BTN = (By.XPATH, "//li//button[text()='Выход']") # Кнопка выход из аккаунта в окне профиля

                    