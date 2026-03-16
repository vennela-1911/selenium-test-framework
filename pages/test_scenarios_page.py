from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ScenariosPage(BasePage):

    ALERT_BTN = (By.ID, "alertBtn")
    CONFIRM_BTN = (By.ID, "confirmBtn")
    PROMPT_BTN = (By.ID, "promptBtn")

    IFRAME = (By.ID, "testFrame")
    NEW_TAB = (By.ID, "newTab")

    def trigger_alert(self):

        self.click(self.ALERT_BTN)
        alert = self.driver.switch_to.alert
        alert.accept()

    def trigger_confirm(self):

        self.click(self.CONFIRM_BTN)
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def trigger_prompt(self):

        self.click(self.PROMPT_BTN)
        alert = self.driver.switch_to.alert
        alert.send_keys("Test Input")
        alert.accept()

    def switch_to_frame(self):

        frame = self.find(self.IFRAME)
        self.driver.switch_to.frame(frame)

    def open_new_tab(self):

        self.click(self.NEW_TAB)