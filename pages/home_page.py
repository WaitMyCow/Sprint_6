from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def click_question(self, question):
        locator = [By.ID, HomePageLocators.QUESTION[1].format(question)]
        element = self.find_element(locator)
        self.scroll_to_element(element)
        self.click_element(locator)

    def is_question_expanded(self, question):
        locator = [By.ID, HomePageLocators.QUESTION[1].format(question)]
        element = self.find_element(locator)
        return element.get_attribute("aria-expanded") == "true"

    def click_order_button_top(self):
        self.click_element(HomePageLocators.ORDER_BUTTON_TOP)

    def click_order_button_big(self):
        locator = HomePageLocators.ORDER_BUTTON_BIG
        element = self.find_element(locator)
        self.scroll_to_element(element)
        self.click_element(locator)