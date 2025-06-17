import allure
import pytest

import data
import helper
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestCreateOrders:
    @allure.title("Проверка оформления заказа")
    @allure.description("Выполение процесса создания заказа от начала до конца")
    @pytest.mark.parametrize("button", data.Data.orders)
    def test_create_order(self, driver, button):
        main_page = MainPage(driver)
        main_page.click_on_order(button)
        order_page = OrderPage(driver)
        order_page.fill_scooter_fields(*helper.generate_order_field())
        order_page.click_next_scooter()
        order_page.fill_rental_fields(*helper.generate_rental_field())
        order_page.click_next_rental()
        order_page.confirm_created_order()
        order_page.check_created_order()
