from behave import given, when, then
from pages.login_page import LoginPage
from settings.config import settings
from allocator.driver import driver

@Given('I am on the saucedemo loginpage')
def validate_login_page(context):
    driver.navigate(settings.url)
    result = LoginPage.validate_login_page(context)
    assert result is True

@when('I enter username "{username}" and I enter password "{pwd}"')
def enter_username_and_password(context, username, pwd):
    #driver.navigate(settings.url)
    result = LoginPage.enter_username_and_password(context, username, pwd)
    assert result is True

@when('I click login button')
def click_on_add_button(context):
    #driver.navigate(settings.url)
    result = LoginPage.click_on_add_button(context)

@then('I am logged in')
def see_login_message(context):
    #driver.navigate(settings.url)
    result = LoginPage.see_login_message(context)
    
