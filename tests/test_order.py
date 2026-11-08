from pages.home_page import HomePage
import pytest
import allure
from utils import Utils
from urls import Urls
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators

@allure.feature('Проверка оформления заказа')
class TestOrder:
    @allure.title('Проверка заполнения данных и успешного оформления заказа')
    @pytest.mark.parametrize("order_button, name, surname, address, metro, phone, date, period", Utils.order_data())
    def test_order(self, driver, order_button, name, surname, address, metro, phone, date, period):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        if order_button == "top": #для каждого набора данных своя кнопка. Как итог 2 теста
            home_page.click_order_button_top()
        else:
            home_page.click_order_button_big()
        order_page.create_order(name, surname, address, metro, phone, date, period)

        assert order_page.is_order_successful()

    @allure.title('Проверка нажатия на лого {logo} после оформления заказа')
    @pytest.mark.parametrize("logo", [OrderPageLocators.SCOOTER_LOGO, OrderPageLocators.YANDEX_LOGO])
    def test_logo_click(self, driver, logo):
        home_page = HomePage(driver)
        if logo == OrderPageLocators.SCOOTER_LOGO:
            home_page.click_element(logo)

            assert home_page.get_current_url() == Urls.BASE_URL

        elif logo == OrderPageLocators.YANDEX_LOGO:
            old_windows = home_page.get_window_handles()
            home_page.click_element(logo)
            home_page.switch_to_new_window(old_windows)
            home_page.wait_for_url_contains(Urls.DZEN_URL)

            assert home_page.get_current_url() == Urls.DZEN_URL
                