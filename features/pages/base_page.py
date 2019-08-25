from selenium import webdriver
from features.data.read import GetEnvironmentInfo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Browser(object):
    print("Browser Invoked")
    driver = webdriver.Firefox(executable_path=GetEnvironmentInfo.GLOBAL_DRIVER)
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    driver.maximize_window()

    def close(context):
        context.driver.close()

    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def check_element(self, *locator):
        self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def wait_til_visible(self, *locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.driver.find_element(*locator)))
