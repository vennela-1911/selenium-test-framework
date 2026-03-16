from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_element

class UsersPage:

    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    USER_HEADER = (By.XPATH, "//h6[text()='User Management']")

    def __init__(self, driver):
        self.driver = driver

    def open_users_page(self):
        wait_for_element(self.driver, self.ADMIN_MENU).click()

    def is_users_page_open(self):
        return wait_for_element(self.driver, self.USER_HEADER) is not None