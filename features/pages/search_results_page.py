from selenium.webdriver.common.by import By
from features.pages import Browser


class SearchResultsPageLocator(object):

    PAGE_TITLE = (By.XPATH, "//title")


class SearchResultsPage(Browser):

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def find_search_result(self, search_result):
        #search_result = "/html//main[@id='content']//form[@action='/search/']//ul[@class='unstyled']//a[@href='/project/behave/']/h3[@class='package-snippet__title']"
        return self.get_element(By.XPATH, search_result)

