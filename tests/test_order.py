from pages.home_page import HomePage
import pytest
import allure
from utils import Utils
from urls import Urls
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators

@allure.feature('Проверка оформления заказа')
class TestOrder:
    @allure.title('Проверка заполнения данных и успешного оформления заказа')
    @pytest.mark.parametrize("order_button, name, surname, address, metro, phone, date, period", Utils.order_data())
    def test_order(self, driver, order_button, name, surname, address, metro, phone, date, period):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_order_button(order_button)
        order_page.create_order(name, surname, address, metro, phone, date, period)

        assert order_page.is_order_successful()

    @allure.title('Проверка нажатия на лого {logo} после оформления заказа')
    @pytest.mark.parametrize("logo, expected_url",[(HomePageLocators.SCOOTER_LOGO, Urls.BASE_URL),(HomePageLocators.YANDEX_LOGO, Urls.DZEN_URL)])
    def test_logo_click(self, driver, logo, expected_url):
        home_page = HomePage(driver)
        home_page.click_logo(logo)

        assert home_page.get_current_url() == expected_url
                