from selenium.webdriver.common.by import By


class MainPageLocators:
    # Верхнее меню
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

    # Кнопки на главной
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Вкладки конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")


class LoginLocators:
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    RESTORE_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")


class RegistrationLocators:
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")


class AccountLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LOGO_LINK = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")


class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
