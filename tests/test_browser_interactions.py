BASE_URL = "https://react-frontend-api-testing.vercel.app/login"


def test_page_title(driver):

    driver.get(BASE_URL)

    assert "api backend dashboard" in driver.title.lower()


def test_refresh(driver):

    driver.get(BASE_URL)

    driver.refresh()

    assert "vercel.app" in driver.current_url