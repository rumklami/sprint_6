import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открыть вопрос раздела О важном")
    def click_on_question(self, question):
        question_locator = MainPageLocators.text_question(question)
        self.scroll_into_view(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Сравнить ответ раздела О важном")
    def check_answer(self, question, expected_text):
        answer_locator = MainPageLocators.text_answer(question)
        actual_answer = self.get_text_element(answer_locator)
        assert expected_text == actual_answer

    @allure.step("Нажать кнопку Заказать")
    def click_on_order(self, order):
        self.scroll_into_view(order)
        self.click_on_element(order)

    @allure.step("Проверка перехода по ссылке")
    def check_follow_link(self, locator_link, expected_link, locator_wait):
        self.click_on_element(locator_link)
        self.switch_active_window(locator_wait)
        text_link = self.get_address_page()
        assert text_link == expected_link
