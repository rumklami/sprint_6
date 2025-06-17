import allure
import pytest

import data

from pages.main_page import MainPage


class TestListOfQuestion:
    @allure.title("Проверка ответов на вопросы раздела О важном")
    @allure.description("Раскрытие списка и проверка текста ответов на вопросы")
    @pytest.mark.parametrize("question, answer", data.Data.question)
    def test_list_of_question(self, driver, question, answer):
        main_page = MainPage(driver)
        main_page.click_on_question(question)
        main_page.check_answer(question, answer)
