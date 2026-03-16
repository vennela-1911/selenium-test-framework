import pytest
from selenium import webdriver
from utils.logger import get_logger

logger = get_logger()


@pytest.fixture
def driver():

    logger.info("Launching browser")

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    logger.info("Closing browser")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        driver = item.funcargs.get("driver", None)

        if driver:

            import os

            os.makedirs("reports/screenshots", exist_ok=True)

            status = "PASS" if report.passed else "FAIL"

            screenshot_name = f"reports/screenshots/{item.name}_{status}.png"

            driver.save_screenshot(screenshot_name)

            logger.info(f"Screenshot saved: {screenshot_name}")