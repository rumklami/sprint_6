import pytest
from selenium import webdriver

from curl import main_page


@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.get(main_page)
    yield browser
    browser.quit()
