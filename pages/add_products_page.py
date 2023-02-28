from allocator.web import Web
from pages.locators_add_products import LocatorsAddProducts
import time

class ProductsPage(Web):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ProductsPage()
        return cls.instance

    def __init__(self):
        super().__init__()


    def see_home_message(self, context):
        message = super().get_text_xpath(self, LocatorsAddProducts.locators["xpath_header_products"])
        if message == "Products":
            return True
        return False

    def look_product(self, context):
        message = super().get_text_xpath(self, LocatorsAddProducts.locators["xpath_product1"])
        if message == "ProdSauce Labs Bolt T-Shirt":
            return True
        return False

    def add_product1(self, context):
        message = super().click_by_id(self, LocatorsAddProducts.locators["id_btn_product1"])
        time.sleep(2)

    def verify_cart(self, context):
        message = super().click_by_xpath(self, LocatorsAddProducts.locators["xpath_cart"])
        time.sleep(2)
        message2 = super().get_text_xpath(self, LocatorsAddProducts.locators["xpath_product1_in_the_cart"])
        if message2 == "Sauce Labs Bolt T-Shirt":
            return True
        return False



ProductsPage = ProductsPage.get_instance()