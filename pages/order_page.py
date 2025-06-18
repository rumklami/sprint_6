import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполнить поля заказа Для кого самокат")
    def fill_scooter_fields(self, text_name, text_second_name, text_address, metro_id, text_phone):
        self.send_keys_to_element(OrderPageLocators.NAME, text_name)
        self.send_keys_to_element(OrderPageLocators.MIDDLE_NAME, text_second_name)
        self.send_keys_to_element(OrderPageLocators.ADDRESS, text_address)
        self.choose_element_of_list(OrderPageLocators.METRO, OrderPageLocators.metro(metro_id))
        self.send_keys_to_element(OrderPageLocators.PHONE_NUMBER, text_phone)

    @allure.step("Нажать кнопку Далее в форме Для кого самокат")
    def click_next_scooter(self):
        self.click_on_element(OrderPageLocators.NEXT)

    @allure.step("Заполнить поля Про аренду")
    def fill_rental_fields(self, when, period_id, color, comment):
        self.send_keys_to_element(OrderPageLocators.WHEN, when)
        self.click_on_element(color)
        self.choose_element_of_list(OrderPageLocators.PERIOD, OrderPageLocators.period(period_id))
        self.send_keys_to_element(OrderPageLocators.COMMENT, comment)

    @allure.step("Нажать кнопку Далее в форме Про аренду")
    def click_next_rental(self):
        self.click_on_element(OrderPageLocators.CREATE_ORDER)

    @allure.step("Подтвердить оформление заказа")
    def confirm_created_order(self):
        self.click_on_element(OrderPageLocators.COMPLETE)

    @allure.step("Проверка созданного заказа")
    def check_created_order(self, expected_text="Заказ оформлен"):
        text_message = self.get_text_element(OrderPageLocators.ORDER_PLACED)
        assert expected_text in text_message
