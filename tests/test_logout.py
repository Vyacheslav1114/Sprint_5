import time
from pages.locators import AccountLocators as A
from helpers import generate_email, generate_password

BASE = "https://stellarburgers.education-services.ru/"

def register_login_and_logout(driver):
    # регистрация + логин (встроено)
    from pages.locators import RegistrationLocators as R, LoginLocators as L
    # регистрация
    driver.get(f"{BASE}/register")
    email = generate_email()
    password = generate_password()
    driver.find_element(*R.NAME_INPUT).send_keys("QA")
    driver.find_element(*R.EMAIL_INPUT).send_keys(email)
    driver.find_element(*R.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*R.REGISTER_BUTTON).click()
    time.sleep(1)
    # логин
    driver.get(f"{BASE}/login")
    driver.find_element(*L.EMAIL_INPUT).send_keys(email)
    driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*L.LOGIN_SUBMIT).click()
    time.sleep(1)
    return email, password

def test_logout(driver):
    register_login_and_logout(driver)
    driver.get(f"{BASE}/account")
    driver.find_element(*A.PROFILE_LOGOUT).click()
    time.sleep(1)
    # ожидаем возврат на страницу логина
    assert "login" in driver.current_url
