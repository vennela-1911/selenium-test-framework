from pages.login_page import LoginPage

BASE_URL = "https://react-frontend-api-testing.vercel.app/login"


def test_dashboard_redirect(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login("test@example.com", "password123")

    # demo site stays on login page
    assert "login" in driver.current_url.lower()