from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allocator.driver import driver

class Web:
    __TIMEOUT = 10

    def __init__(self):
        self.driver = driver.get_driver()

    def open(self, url):
        self.driver.get(url)

    def maximize(self):
        self.driver.maximize_window()

    def title(self):
        return self.driver.title

    def curent_url(self):
        return self.driver.current_url

    @staticmethod
    def get_text_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).text

    def find_by_xpath(self, xpath):
        return self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def finds_by_xpath(self, xpath):
        return self.driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def find_by_xpath_displayed(self, xpath):
        return self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).is_displayed()

    def find_by_name(self, name):
        return self.driver.find_element(By.NAME, name)

    @staticmethod
    def finds_by_name(self, name):
        return self.driver_wait.until(EC.presence_of_all_elements_located((By.NAME, name)))

    @staticmethod   
    def find_by_id(self, id):
        return self.driver.find_element(By.ID, id)

    @staticmethod   
    def click_by_id(self, id):
        return self.driver.find_element(By.ID, id).click()

    @staticmethod   
    def click_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).click()

    def find_by_id_displayed(self, id_value):
        return self.driver_wait.until(EC.presence_of_element_located((By.ID, id_value))).is_displayed()

    def finds_by_id(self, id):
        return self.driver_wait.until(EC.presence_of_all_elements_located((By.ID, id)))

    def find_by_class_name(self, classname):
        return self.driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, classname)))

    def finds_by_class_nam(self, classname):
        return self.driver_wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, classname)))

    def find_by_css_selector(self, cssselector):
        return self.driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, cssselector)))

    def finds_by_css_selector(self, cssselector):
        return self.driver_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, cssselector)))

    def switch_frame(self,frame):
        return self.driver.switch_to.frame(frame)

    def close(self):
        self.driver.quit()

web = Web()