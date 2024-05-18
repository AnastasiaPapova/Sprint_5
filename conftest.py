import pytest
from selenium import webdriver
import locators
from main.burger_urls import Urls
from main.user_data import UserData


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,990")
    return chrome_options


@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(Urls.BASE_URL)
    yield chrome
    chrome.quit()


@pytest.fixture
def login(driver):
    driver.get(Urls.LOGIN_PAGE)
    driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(UserData.SIGN_IN_LOGIN)
    driver.find_element(*locators.LOGIN_PASSWD_INPUT).send_keys(UserData.SIGN_IN_PASSWD)
    driver.find_element(*locators.LOGIN_BUTTON).click()
    driver.implicitly_wait(2)
    driver.find_element(*locators.CREATE_ORDER_BUTTON).is_displayed()

