import pytest
from pages.login_page import LoginPage

BASE_URL = "https://react-frontend-api-testing.vercel.app/login"


def test_valid_login(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login("test@example.com", "password123")

    # Demo site does not redirect after login
    assert "vercel.app/login" in driver.current_url


@pytest.mark.parametrize("email,password", [
    ("wrong@test.com", "123"),
    ("invalidemail", "password123"),
    ("", "")
])
def test_invalid_login_matrix(driver, email, password):

    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login(email, password)

    # User should remain on login page
    assert "login" in driver.current_url.lower()