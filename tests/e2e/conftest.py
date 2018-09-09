import pytest
from selenium import webdriver
from tests.e2e.page_objects import LoginPage


@pytest.fixture
def driver():
    return webdriver.Firefox()

@pytest.fixture()
def LoginPageObject(driver):
    # TODO abstract URI
    page = LoginPage(driver, root_uri="https://splashthat.com")
    page.get("/login")
    return page
