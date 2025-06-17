from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма Для кого самокат
    NAME = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    MIDDLE_NAME = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]")
    ADDRESS = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")
    METRO = (By.XPATH, "//input[contains(@placeholder,'Станция метро')]")
    PHONE_NUMBER = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")
    NEXT = (By.XPATH, "//button[text() = 'Далее']")

    # Форма Про аренду
    WHEN = (By.XPATH, "//input[contains(@placeholder,'Когда привезти самокат')]")
    PERIOD = (By.XPATH, "//*[@class='Dropdown-root']")
    BLACK = (By.XPATH, "//*[@id='black']")
    GREY = (By.XPATH, "//*[@id='grey']")
    COMMENT = (By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]")
    CREATE_ORDER = (By.XPATH, "//*[contains(@class,'Order_Buttons')]/button[text()='Заказать']")

    # Форма Подтверждения заказа
    COMPLETE = (By.XPATH, "//*[contains(@class,'Order_Buttons')]/button[text()='Да']")

    # Заказ оформлен
    ORDER_PLACED = (By.XPATH, "//*[text()='Заказ оформлен']")

    @staticmethod
    def period(period_id):
        return By.XPATH, f"//*[@class='Dropdown-menu']/div[{period_id}]"

    @staticmethod
    def metro(metro_id):
        return By.XPATH, f"//ul[@class = 'select-search__options']/li[@data-index='{metro_id}']"
