import pytest
from selenium import webdriver
from tests.e2e.consts import root_uri
from tests.e2e.page_objects import LoginPage


@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    yield driver

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)

@pytest.fixture()
def LoginPageObject(driver):
    # TODO abstract URI
    page = LoginPage(driver, root_uri=root_uri)
    page.load()
    return page
