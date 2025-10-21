import time
from pages.locators import RegistrationLocators as L
from helpers import generate_email, generate_password

BASE = "https://stellarburgers.education-services.ru"

def test_successful_registration(driver):
    """Успешная регистрация: пустое имя запрещено проверяется вводом непустого имени"""
    driver.get(f"{BASE}/register")
    email = generate_email()
    password = generate_password()

    driver.find_element(*L.NAME_INPUT).send_keys("Тест")
    driver.find_element(*L.EMAIL_INPUT).send_keys(email)
    driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*L.REGISTER_BUTTON).click()

    # ожидаем переход на страницу логина (в URL встречается 'login' или появление кнопки 'Войти')
    time.sleep(2)
    assert ("login" in driver.current_url) or (driver.find_elements_by_xpath("//button[text()='Войти']")), "Регистрация не привела на страницу логина"

def test_invalid_password_shows_error(driver):
    driver.get(f"{BASE}/register")
    driver.find_element(*L.NAME_INPUT).send_keys("Тест")
    driver.find_element(*L.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*L.PASSWORD_INPUT).send_keys("123")  # короткий пароль
    driver.find_element(*L.REGISTER_BUTTON).click()
    time.sleep(1)
    # проверяем наличие сообщения об ошибке
    elems = driver.find_elements(*L.PASSWORD_ERROR)
    assert len(elems) > 0, "Ошибка о некорректном пароле не показана"
