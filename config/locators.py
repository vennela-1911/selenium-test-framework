from selenium.webdriver.common.by import By

class LoginLocators:

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")


class DashboardLocators:

    USER_ROLE = (By.ID, "userRole")


class UsersLocators:

    USERS_TABLE = (By.ID, "usersTable")
    ACCESS_DENIED = (By.ID, "accessDenied")