from behave import *
from nose.tools import assert_equal, assert_true
from features.data.read import GetEnvironmentInfo


@step('I navigate to the homepage')
def step_impl(context):
    context.home_page.navigate(GetEnvironmentInfo.GLOBAL_URL)
    assert_equal(context.home_page.get_page_title(), "OrangeHRM")


@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)


@step('I am taken to the PyPi Search Results page')
def step_impl(context):
    assert_equal(context.search_results_page.get_page_title(), "Search results · PyPI")


@step('I see a search result for "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result))
