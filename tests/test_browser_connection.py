from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_browser_connection():
    options = webdriver.ChromeOptions()
    # Отключаем headless, чтобы увидеть браузер
    # options.add_argument("--headless")  # не включаем!
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        driver.get("https://stellarburgers.education-services.ru/")
        print("Title:", driver.title)
        time.sleep(3)
    finally:
        driver.quit()
