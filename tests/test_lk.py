import locators
from main.burger_urls import Urls
from conftest import driver, login


class TestBurgerLK:

    def test_lk_page(self, driver, login):
        driver.find_element(*locators.lk_button).click()
        order_history = driver.find_element(*locators.order_history_button_in_lk)
        assert driver.current_url == Urls.profile_page and order_history.text == 'История заказов'

    def test_click_constructor_form_in_lk_page(self, driver, login):
        driver.find_element(*locators.lk_button).click()
        driver.find_element(*locators.constructor_button_in_lk_page).click()
        constructor_header = driver.find_element(*locators.constructor_page_header)
        assert constructor_header.text == "Соберите бургер"

    def test_constructor_from_after_click_logo(self, driver, login):
        driver.find_element(*locators.lk_button).click()
        driver.find_element(*locators.logo_button).click()
        constructor_header = driver.find_element(*locators.constructor_page_header)
        assert constructor_header.text == "Соберите бургер"

    def test_logout_with_lk_page(self, driver, login):
        driver.find_element(*locators.lk_button).click()
        driver.find_element(*locators.logout_button).click()
        login_page = driver.find_element(*locators.login_page)
        assert driver.current_url == Urls.login_page and login_page.text == "Вход"



