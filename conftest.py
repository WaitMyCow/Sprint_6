from selenium import webdriver
from urls import Urls
import pytest


@pytest.fixture(scope="function") #scope - время жизни фикстуры. В данном случае она перезапускается для каждого теста (функции)
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()