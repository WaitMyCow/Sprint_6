from pages.home_page import HomePage
import pytest
import allure
from utils import Utils


#Выпадающий список в разделе «Вопросы о важном».
@allure.feature('Проверка выпадающего списка «Вопросы о важном» на главной странице')
class TestDropDownList:
    #Важно написать отдельный тест на каждый вопрос.
    @allure.title('Проверка вопроса: {question_text}')
    @pytest.mark.parametrize("question_number, question_text, answer_text", Utils.questions_text())
    def test_questions_expands(self, driver, question_number, question_text, answer_text):
        home_page = HomePage(driver)
        home_page.click_question(question_number)
        actual_answer = home_page.get_answer_text(question_number)
        assert actual_answer == answer_text