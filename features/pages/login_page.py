from selenium.webdriver.common.by import By
from features.pages.base_page import Browser


class LoginPageLocator(object):

    USERNAME_FIELD = (By.XPATH, "/html//input[@id='txtUsername']")
    PASSWORD_FIELD = (By.XPATH, "/html//input[@id='txtPassword']")
    WELCOME_LABEL = (By.CSS_SELECTOR, "#welcome")
    LOGIN_BUTTON = (By.XPATH, "/html//input[@id='btnLogin']")


class LoginPage(Browser):
    def login(self, username, password):
        self.input(username, *LoginPageLocator.USERNAME_FIELD)
        self.input(password, *LoginPageLocator.PASSWORD_FIELD)
        self.click_element(*LoginPageLocator.LOGIN_BUTTON)

    def check_homepage(self):
        assert self.driver.find_element(*LoginPageLocator.WELCOME_LABEL)
