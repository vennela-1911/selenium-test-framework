from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_element

class DashboardPage:

    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_loaded(self):
        element = wait_for_element(self.driver, self.DASHBOARD_HEADER)
        return element is not None