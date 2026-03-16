from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def create_driver():

    browser = os.getenv("BROWSER", "chrome")
    grid_url = os.getenv("GRID_URL")

    options = Options()

    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless")

    if grid_url:
        driver = webdriver.Remote(
            command_executor=grid_url,
            options=options
        )
    else:
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    return driver