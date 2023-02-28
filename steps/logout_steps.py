from behave import given, when, then
from pages.logout_page import LogoutPage
from settings.config import settings
from allocator.driver import driver

@Given('I am logged on the saucedemo')
def see_home_message(context):
    #driver.navigate(settings.url)
    result = LogoutPage.see_home_message(context)
    #assert result is True

@when('I click in menu button')
def click_on_menu_button(context):
    #driver.navigate(settings.url)
    result = LogoutPage.click_on_menu_button(context)

@when('I click in link logout')
def click_on_logout_item(context):
    #driver.navigate(settings.url)
    result = LogoutPage.click_on_logout_item(context)

@then('return to login page')
def validate_login_page(context):
    #driver.navigate(settings.url)
    result = LogoutPage.validate_login_page(context)
    assert result is True
    
