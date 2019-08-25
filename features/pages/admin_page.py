from selenium.webdriver.common.by import By
from features.pages.base_page import Browser


class AdminPageLocator(object):

    USERNAME_FIELD = (By.XPATH, "/html//input[@id='txtUsername']")

    ADMIN_TAB = (By.ID, "menu_admin_viewAdminModule")
    USER_MANAGEMENT_MENU = (By.ID, "menu_admin_UserManagement")
    USER_MENU = (By.ID, "menu_admin_viewSystemUsers")
    SYSTEM_USERS_PAGE = (By.ID, "systemUser-information")

    ADD_BUTTON = (By.ID, "btnAdd")
    ADD_PAGE = (By.ID, "systemUser")
    USER_ROLE_SELECT = (By.ID, "systemUser_userType")
    USER_EMPLOYEE_NAME_FIELD = (By.ID, "systemUser_employeeName_empName")
    USER_NAME_FIELD = (By.ID, "systemUser_userName")
    USER_STATUS_SELECT = (By.ID, "systemUser_status")
    USER_PASSWORD = (By.ID, "systemUser_password")
    USER_CONFIRM_PASSWORD = (By.ID, "systemUser_confirmPassword")


class AdminPage(Browser):

    def goto_user_management(self):
        # Nope. Too Complicated?
        self.click_element(*AdminPageLocator.ADMIN_TAB)
        self.click_element(*AdminPageLocator.ADMIN_TAB)
        self.click_element(*AdminPageLocator.ADMIN_TAB)
        self.click_element(*AdminPageLocator.USER_MANAGEMENT_MENU)
        self.click_element(*AdminPageLocator.USER_MANAGEMENT_MENU)
        self.click_element(*AdminPageLocator.USER_MANAGEMENT_MENU)
        self.wait_til_visible(*AdminPageLocator.SYSTEM_USERS_PAGE)

    def get(self):
        def func_not_found():  # just in case we dont have the function
            print('No Function ' + self.i + ' Found!')
        func_name = 'function' + self.i
        func = getattr(self, func_name, func_not_found)
        func()
        return func()