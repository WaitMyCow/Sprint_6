from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON_TOP = [By.XPATH, "//button[text()='Заказать' and not(contains(@class, 'Button_UltraBig'))]"]
    ORDER_BUTTON_BIG = [By.XPATH, "//button[contains(@class, 'Button_Middle')]"]
    QUESTION = [By.ID, "accordion__heading-{}"]
    QUESTION_EXPANDED = [By.XPATH, "//*[@aria-expanded='true']"]