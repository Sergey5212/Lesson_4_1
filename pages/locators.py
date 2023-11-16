from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
