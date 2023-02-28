from allocator.web import Web
from pages.locators_login import LocatorsLogin
import time

class LoginPage(Web):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def validate_login_page(self, context):
        message = super().get_text_xpath(self, LocatorsLogin.locators["xpath_users_name"])
        time.sleep(1)
        if message == "Accepted usernames are:":
            return True
        return False

    def enter_username_and_password(self, context, username, pwd):

        print("enter_username_and_password...") 
        usernameTemp = super().find_by_id(self, LocatorsLogin.locators["id_username"])
        passwordTemp = super().find_by_id(self, LocatorsLogin.locators["id_password"])
        
        if usernameTemp != None and passwordTemp != None:
            super().find_by_id(self, LocatorsLogin.locators["id_username"]).send_keys(username)
            super().find_by_id(self, LocatorsLogin.locators["id_password"]).send_keys(pwd)
            time.sleep(3)
            return True
        return False

    def click_on_add_button(self, context):
        message = super().click_by_id(self, LocatorsLogin.locators["id_btn_login"])
        time.sleep(3)

    def see_login_message(self, context):
        message = super().get_text_xpath(self, LocatorsLogin.locators["xpath_header_products"])
        if message == "Products":
            return True
        return False
        


LoginPage = LoginPage.get_instance()
