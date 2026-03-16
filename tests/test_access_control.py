from pages.login_page import LoginPage

BASE_URL = "https://react-frontend-api-testing.vercel.app/login"


def test_admin_users_page(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login("test@example.com", "password123")

    assert "login" in driver.current_url.lower()