import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    @allure.step("Ожидание загрузки элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Заполнение полей элемента")
    def send_keys_to_element(self, locator, text):
        self.wait_for_element(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Скролл до элемента")
    def scroll_into_view(self, locator):
        self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    @allure.step("Снять фокус с поля")
    def remove_focus_field(self):
        self.driver.execute_script("document.activeElement.blur();")

    @allure.step("Получить сообщение из элемента")
    def get_text_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator).text

    @allure.step("Подождать загрузку страницы")
    def wait_loading_window(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    @allure.step("Получить адрес страницы")
    def get_address_page(self):
        self.wait_loading_window()
        return self.driver.current_url

    @allure.step("Переключение на активное окно страницы")
    def switch_active_window(self, locator):
        self.wait_loading_window()
        current_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                self.wait_for_element(locator)
                break

    @allure.step("Выбор элемента с открытием списка")
    def choose_element_of_list(self, locator_field, locator_element):
        self.click_on_element(locator_field)
        self.scroll_into_view(locator_element)
        self.click_on_element(locator_element)
