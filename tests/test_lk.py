import locators
from main.burger_urls import Urls
from conftest import driver, login


class TestBurgerLK:

    def test_lk_page(self, driver, login):
        driver.find_element(*locators.LK_BUTTON).click()
        order_history = driver.find_element(*locators.ORDER_HISTORY_BUTTON_IN_LK_PAGE)
        assert driver.current_url == Urls.PROFILE_PAGE and order_history.text == 'История заказов'


    def test_click_constructor_form_in_lk_page(self, driver, login):
        driver.find_element(*locators.LK_BUTTON).click()
        driver.find_element(*locators.CONSTRUCTOR_BUTTON_IN_LK_PAGE).click()
        constructor_header = driver.find_element(*locators.CONSTRUCTOR_PAGE_HEADER)
        assert constructor_header.text == "Соберите бургер"


    def test_constructor_from_after_click_logo(self, driver, login):
        driver.find_element(*locators.LK_BUTTON).click()
        driver.find_element(*locators.LOGO_BUTTON).click()
        constructor_header = driver.find_element(*locators.CONSTRUCTOR_PAGE_HEADER)
        assert constructor_header.text == "Соберите бургер"


    def test_logout_with_lk_page(self, driver, login):
        driver.find_element(*locators.LK_BUTTON).click()
        driver.find_element(*locators.LOGOUT_BOTTON).click()
        login_page = driver.find_element(*locators.LOGIN_PAGE)
        assert driver.current_url == Urls.LOGIN_PAGE and login_page.text == "Вход"



