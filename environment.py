from allocator.driver import driver
from settings.config import settings
from behave.model_core import Status

def after_all(context):
    driver.stop_instance()

def before_scenario(context, scenario):
    driver.clear_cookies()

