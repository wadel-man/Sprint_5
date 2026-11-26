import random
login = 'ravil_askyanov_58'
USER_EMAIL = 'bandercha2255@gmail.com'
USER_PASSWORD = '12345678'


def generate_login():
    generate_login_int = random.randint(100,999)
    return f'{login}_{generate_login_int}@yandex.ru'


def generate_password():
    password = random.randint(100000,999999)
    return f'{password}'


