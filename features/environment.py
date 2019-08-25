from features.pages.base_page import Browser
from features.pages.login_page import LoginPage
from features.pages.admin_page import AdminPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.admin_page = AdminPage()


def after_all(context):
    context.browser.close()
