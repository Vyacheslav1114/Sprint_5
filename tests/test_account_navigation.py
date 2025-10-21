import time
from pages.locators import MainPageLocators as M, AccountLocators as A
from helpers import generate_email, generate_password

BASE = "https://stellarburgers.education-services.ru/"

# Для тестов личного кабинета нам нужен действующий пользователь.
# В рамках задания: тесты автономны. Здесь можно зарегистрировать пользователя на ходу,
# затем войти и протестировать переходы.
def register_and_login(driver):
    # регистрация
    driver.get(f"{BASE}/register")
    email = generate_email()
    password = generate_password()
    driver.find_element(*A.CONSTRUCTOR_LINK)  # just to ensure page is loaded (no-op)
    driver.find_element(*A.CONSTRUCTOR_LINK)  # avoid linter warning
    from pages.locators import RegistrationLocators as R
    driver.find_element(*R.NAME_INPUT).send_keys("QA Test")
    driver.find_element(*R.EMAIL_INPUT).send_keys(email)
    driver.find_element(*R.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*R.REGISTER_BUTTON).click()
    time.sleep(1)
    # теперь залогиниться
    driver.get(f"{BASE}/login")
    from pages.locators import LoginLocators as L
    driver.find_element(*L.EMAIL_INPUT).send_keys(email)
    driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*L.LOGIN_SUBMIT).click()
    time.sleep(1)

def test_go_to_account(driver):
    # регистрация + логин внутри теста
    register_and_login(driver)
    # клик на личный кабинет
    driver.find_element(*M.PERSONAL_ACCOUNT).click()
    time.sleep(1)
    assert driver.find_elements(*A.PROFILE_HEADER), "Не перешли в личный кабинет"

def test_from_account_to_constructor_and_logo(driver):
    register_and_login(driver)
    # из кабинета переходим в конструктор
    driver.get(f"{BASE}/account")
    driver.find_element(*A.CONSTRUCTOR_LINK).click()
    time.sleep(1)
    # проверка: нажмём на логотип и ожидаем переход в конструктор (главную)
    driver.find_element(*M.LOGO).click()
    time.sleep(1)
    assert "profile" not in driver.current_url
