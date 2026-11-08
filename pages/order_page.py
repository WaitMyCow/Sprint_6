from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
import allure

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Выбираем станцию метро {metro}')
    def select_metro(self, metro):
        self.click_element(OrderPageLocators.METRO_LIST)
        locator = [By.XPATH, OrderPageLocators.METRO_STATION[1].format(metro)]
        self.click_element(locator)

    @allure.step('Заполняем дату {date}')
    def select_date(self, date):
        locator = [By.XPATH,OrderPageLocators.ORDER_DATE_IN_CALENDAR[1].format(date)]
        self.click_element(locator)

    @allure.step('Заполняем личные данные {name}, {surname}, {address}, {metro}, {phone}')
    def fill_personal_data(self, name, surname, address, metro, phone):
        self.find_element(OrderPageLocators.NAME_FIELD).send_keys(name)
        self.find_element(OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        self.find_element(OrderPageLocators.ADRESS_FIELD).send_keys(address)
        self.select_metro(metro)
        self.find_element(OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем данные аренды {date}, {period}')
    def fill_rental_data(self, date, period):
        self.click_element(OrderPageLocators.ORDER_DATE)
        self.select_date(date)
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        locator = [By.XPATH, OrderPageLocators.RENTAL_PERIOD_LIST[1].format(period)]
        self.click_element(locator)

    @allure.step('Подтверждаем оформление заказа')
    def confirm_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Проверяем успешное оформление заказа')
    def is_order_successful(self):
        self.find_element(OrderPageLocators.ORDER_SUCCESS_MESSAGE)
        return True

    @allure.step('Оформляем заказ')
    def create_order(self, name, surname, address, metro, phone, date, period):
        self.fill_personal_data(name, surname, address, metro, phone)
        self.fill_rental_data(date, period)
        self.confirm_order()