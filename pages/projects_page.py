from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_element

class ProjectsPage:

    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    HEADER = (By.XPATH, "//h6[text()='PIM']")

    def __init__(self, driver):
        self.driver = driver

    def open_projects(self):
        wait_for_element(self.driver, self.PIM_MENU).click()

    def verify_projects_page(self):
        return wait_for_element(self.driver, self.HEADER) is not None