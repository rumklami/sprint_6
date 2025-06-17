from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_HEAD = (By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    ORDER_BODY = (By.XPATH, "//*[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    SCOOTER = (By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]")
    YANDEX = (By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]")
    DZEN = (By.XPATH, "//*[@data-testid='logo']")

    @staticmethod
    def text_question(question):
        return By.XPATH, f"//div[@class='accordion']/div[{question}]//div[contains(@id,'accordion__heading')]"

    @staticmethod
    def text_answer(question):
        return By.XPATH, f"//div[@class='accordion']/div[{question}]//div[contains(@id,'accordion__heading')]/../..//*[@class='accordion__panel']"
