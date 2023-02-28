from behave import given, when, then
from pages.add_products_page import ProductsPage
from settings.config import settings
from allocator.driver import driver

@Given('I am on the saucedemo Products page')
def see_home_message(context):
    #driver.navigate(settings.url)
    result = ProductsPage.see_home_message(context)
    #assert result is True

@when('I am looking for the product Sauce Labs Bolt T-Shirt')
def look_product(context):
    #driver.navigate(settings.url)
    result = ProductsPage.look_product(context)
    #assert result is True

@when('I click add to cart button Sauce Labs Bolt T-Shirt')
def add_product1(context):
    #driver.navigate(settings.url)
    result = ProductsPage.add_product1(context)

@then('Sauce Labs Bolt T-Shirt product is added to cart')
def verify_cart(context):
    driver.navigate(settings.url)
    result = ProductsPage.verify_cart(context)

    
