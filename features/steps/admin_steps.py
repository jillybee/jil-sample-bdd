from behave import *
from nose.tools import assert_equal, assert_true
from features.data.read import GetEnvironmentInfo, GetLoginInfo
from features.pages.admin_page import AdminPageLocator

# ADMIN_TAB = AdminPageLocator.ADMIN_TAB
# USER_MANAGEMENT_MENU = AdminPageLocator.USER_MANAGEMENT_MENU


@step('I click "{item}" menu')
def step_impl(context, item):
    if item.lower() == "admin":
        context.admin_page.click_element(*AdminPageLocator.ADMIN_TAB)
        context.admin_page.click_element(*AdminPageLocator.ADMIN_TAB)
        context.admin_page.click_element(*AdminPageLocator.ADMIN_TAB)

    elif item.lower() == "user management":
        context.admin_page.click_element(*AdminPageLocator.USER_MANAGEMENT_MENU)
        context.admin_page.click_element(*AdminPageLocator.USER_MANAGEMENT_MENU)
        context.admin_page.click_element(*AdminPageLocator.USER_MANAGEMENT_MENU)


@step('"{pagename}" page is displayed')
def step_impl (context, pagename):
    locator = "AdminPageLocator." + pagename
    context.admin_page.wait_til_visible(*locator)
