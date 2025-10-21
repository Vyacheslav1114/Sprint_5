import socket
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_DOMAIN = "stellarburgers.education-services.ru"

@pytest.fixture(scope="session")
def base_url():
    ip = socket.gethostbyname(BASE_DOMAIN)
    print(f"[INFO] Using resolved IP for tests: {ip}")
    return f"https://{ip}"  # открываем по IP

@pytest.fixture
def driver(base_url):
    ip = base_url.split("//")[1]
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    # Маппим домен → IP для SSL
    options.add_argument(f"--host-resolver-rules=MAP {BASE_DOMAIN} {ip}")
    # Разрешаем запросы к IP, но с правильным host
    options.add_argument("--ignore-certificate-errors")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
