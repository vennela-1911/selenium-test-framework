from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login(self, email, password):

        email_field = self.wait.until(
            EC.presence_of_element_located(self.EMAIL)
        )
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD)
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.wait.until(
            EC.presence_of_element_located(self.LOGIN_BUTTON)
        )

        # JS click (more stable for demo site)
        self.driver.execute_script("arguments[0].click();", login_button)