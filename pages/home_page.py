from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from urls import Urls


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

    def click_order_button(self, order_button):
        if order_button == "top":
            self.click_order_button_top()
        else:
            self.click_order_button_big()

    def click_order_button_top(self):
        self.click_element(HomePageLocators.ORDER_BUTTON_TOP)

    def click_order_button_big(self):
        locator = HomePageLocators.ORDER_BUTTON_BIG
        element = self.find_element(locator)
        self.scroll_to_element(element)
        self.click_element(locator)

    def click_logo(self, logo):
        if logo == HomePageLocators.SCOOTER_LOGO:
            self.click_element(logo)
            self.wait_for_url(Urls.BASE_URL)

        elif logo == HomePageLocators.YANDEX_LOGO:
            old_windows = self.get_window_handles()
            self.click_element(logo)
            self.switch_to_new_window(old_windows)
            self.wait_for_url_contains(Urls.DZEN_URL)

    def get_answer_text(self, question_number):
        locator = (HomePageLocators.ANSWER_TEXT[0],HomePageLocators.ANSWER_TEXT[1].format(question_number))
        answer = self.is_element_visible(locator)
        return answer.text
        