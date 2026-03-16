from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TasksPage(BasePage):

    TASK_STATUS = (By.ID, "taskStatus")
    STATUS_DROPDOWN = (By.ID, "statusDropdown")

    def change_status(self):

        self.click(self.STATUS_DROPDOWN)
        self.click(self.TASK_STATUS)