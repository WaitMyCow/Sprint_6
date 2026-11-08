from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.scroll_to_element(element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click() 

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))
    
    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, element):
        self.driver.execute_script("window.scrollBy(0, arguments[0].getBoundingClientRect().top - 200);", element)

    def get_window_handles(self): #Возвращает список идентификаторов вкладок.
        return self.driver.window_handles

    def wait_for_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(EC.url_contains(text))

    def switch_to_new_window(self, old_windows): #переключает окно/вкладку
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > len(old_windows)) #d.window_handles это список идентификаторов всех открытых вкладок и окон браузера.
        self.driver.switch_to.window(self.driver.window_handles[-1])