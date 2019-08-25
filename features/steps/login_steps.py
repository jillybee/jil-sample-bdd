from behave import *
from nose.tools import assert_equal, assert_true
from features.data.read import GetEnvironmentInfo, GetLoginInfo


@step('I login to the application')
def step_impl(context):
    context.login_page.navigate(GetEnvironmentInfo.GLOBAL_URL)
    assert_equal(context.login_page.get_page_title(), "OrangeHRM")
    context.login_page.login(GetLoginInfo.GLOBAL_USERNAME, GetLoginInfo.GLOBAL_PASSWORD)
    context.login_page.check_homepage()


@step('I am taken to the homepage')
def step_impl(context):
    context.login_page.check_homepage()
