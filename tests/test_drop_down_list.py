from pages.home_page import HomePage
import allure

#Выпадающий список в разделе «Вопросы о важном».
@allure.feature('Проверка выпадающего списка «Вопросы о важном» на главной странице')
class TestDropDownList:
    #Важно написать отдельный тест на каждый вопрос.
    @allure.title('Вопрос: Сколько это стоит? И как оплатить?')
    def test_question_0_expands(self, driver):
        home_page = HomePage(driver)
        home_page.click_question(0)
        assert home_page.is_question_expanded(0)

    @allure.title('Вопрос: Хочу сразу несколько самокатов! Так можно?')
    def test_question_1_expands(self, driver):
        home_page = HomePage(driver)
        home_page.click_question(1)
        assert home_page.is_question_expanded(1)

    @allure.title('Вопрос: Как рассчитывается время аренды?')
    def test_question_2_expands(self, driver):
        home_page = HomePage(driver)
        home_page.click_question(2)
        assert home_page.is_question_expanded(2)

    @allure.title('Вопрос: Можно ли заказать самокат прямо на сегодня?')
    def test_question_3_expands(self, driver):
        home_page = HomePage(driver)
        home_page.click_question(3)
        assert home_page.is_question_expanded(3)

    @allure.title('Вопрос: Можно ли продлить заказ или вернуть самокат раньше?')
    def test_question_4_expands(self, driver):
        home_page = HomePage(driver)
        home_page.click_question(4)
        assert home_page.is_question_expanded(4)

    @allure.title('Вопрос: Вы привозите зарядку вместе с самокатом?')
    def test_question_5_expands(self, driver):
        home_page = HomePage(driver)
        home_page.click_question(5)
        assert home_page.is_question_expanded(5)

    @allure.title('Вопрос: Можно ли отменить заказ?')
    def test_question_6_expands(self, driver):
        home_page = HomePage(driver)
        home_page.click_question(6)
        assert home_page.is_question_expanded(6)

    @allure.title('Вопрос: Я жизу за МКАДом, привезёте?')
    def test_question_7_expands(self, driver):
        home_page = HomePage(driver)
        home_page.click_question(7)
        assert home_page.is_question_expanded(7)