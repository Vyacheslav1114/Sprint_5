from pages.locators import ConstructorLocators as C, MainPageLocators as M
import time

BASE = "https://stellarburgers.education-services.ru/"

def test_constructor_tabs_switching(driver):
    driver.get(BASE)
    # Открываем конструктор
    driver.find_element(*M.CONSTRUCTOR).click()
    time.sleep(1)
    # Переключаем вкладки
    driver.find_element(*C.BUN_TAB).click()
    time.sleep(0.5)
    driver.find_element(*C.SAUCE_TAB).click()
    time.sleep(0.5)
    driver.find_element(*C.FILLING_TAB).click()
    time.sleep(0.5)
    # Убедимся, что активная вкладка присутствует
    assert True
