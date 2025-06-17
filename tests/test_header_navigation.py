import allure
import pytest

import data
from pages.main_page import MainPage


class TestHeaderNavigation:
    @allure.title("Проверка навигации в хеддере в левой части страницы")
    @allure.description("Проверка перехода по кнопкам Яндекс и Самокат")
    @pytest.mark.parametrize("locator_button, address_link, load_button", data.Data.header)
    def test_navigation_yandex(self, driver, locator_button, address_link, load_button):
        main_page = MainPage(driver)
        main_page.check_follow_link(locator_button, address_link, load_button)
