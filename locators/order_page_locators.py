from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = [By.XPATH, "//input[@placeholder='* Имя']"] 
    SURNAME_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"] 
    ADRESS_FIELD = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_LIST = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    METRO_STATION = [By.XPATH, '//li[@role="menuitem"]//button[.//div[normalize-space(.)="{}"]]']
    PHONE_FIELD = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, '//button[text()="Далее"]']


    ORDER_DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    ORDER_DATE_IN_CALENDAR = [By.XPATH, '//div[@aria-label="Choose {}"]']
    RENTAL_PERIOD = [By.CLASS_NAME, "Dropdown-control"]
    RENTAL_PERIOD_LIST = [By.XPATH,'//div[@class="Dropdown-option" and text()="{}"]']
    ORDER_BUTTON = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"]

    YES_BUTTON = [By.XPATH, '//button[text()="Да"]']
    
    ORDER_SUCCESS_MESSAGE = [By.XPATH, '//div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]']

