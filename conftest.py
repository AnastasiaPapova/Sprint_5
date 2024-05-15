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
    chrome.get("https://stellarburgers.nomoreparties.site")

    yield chrome
    chrome.quit()

@pytest.fixture
def login(driver):
    driver.get(Urls.login_page)
    driver.find_element(*locators.login_email_input).send_keys(UserData.sign_in_login)
    driver.find_element(*locators.login_passwd_input).send_keys(UserData.sign_in_passwd)
    driver.find_element(*locators.login_button).click()
    driver.implicitly_wait(2)
    driver.find_element(*locators.create_order_button).is_displayed()

