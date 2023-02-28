from allocator.web import Web
from pages.locators_logout import LocatorsLogout
import time

class LogoutPage(Web):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LogoutPage()
        return cls.instance

    def __init__(self):
        super().__init__()


    def see_home_message(self, context):
        message = super().get_text_xpath(self, LocatorsLogout.locators["xpath_header_products"])
        if message == "Products":
            return True
        return False

    def click_on_menu_button(self, context):
        message = super().click_by_id(self, LocatorsLogout.locators["id_btn_menu"])
        time.sleep(2)

    def click_on_logout_item(self, context):
        message = super().click_by_id(self, LocatorsLogout.locators["id_btn_logout"])
        time.sleep(2)

    def validate_login_page(self, context):
        message = super().get_text_xpath(self, LocatorsLogout.locators["xpath_users_name"])
        time.sleep(1)
        if message == "Accepted usernames are:":
            return True
        return False

LogoutPage = LogoutPage.get_instance()