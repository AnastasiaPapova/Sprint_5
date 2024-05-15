import locators
from conftest import driver
from conftest import login
from main.burger_urls import Urls
from main.user_data import UserData


class TestBurgerLogin:
    def test_login_successfull(self, driver, login):
        # Проверка успешного входа
        create_order_button = driver.find_element(*locators.create_order_button)

        assert driver.current_url == Urls.main_page and create_order_button.text == 'Оформить заказ'

    def test_login_with_lk_button(self, driver):
        # Проверка успешного входа по кнопке личного кабинета
        driver.get(Urls.main_page)
        driver.find_element(*locators.lk_button).click()
        driver.find_element(*locators.login_email_input).send_keys(UserData.sign_in_login)
        driver.find_element(*locators.login_passwd_input).send_keys(UserData.sign_in_passwd)
        driver.find_element(*locators.login_button).click()
        driver.implicitly_wait(2)
        create_order_button = driver.find_element(*locators.create_order_button)

        assert driver.current_url == Urls.main_page and create_order_button.text == 'Оформить заказ'

    def test_login_with_login_button_in_main_page(self, driver):
        # Проверка успешного входа по кнопке "Войти в аккаунт" на главной странице
        driver.get(Urls.main_page)
        driver.find_element(*locators.login_button_in_main_page).click()
        driver.find_element(*locators.login_email_input).send_keys(UserData.sign_in_login)
        driver.find_element(*locators.login_passwd_input).send_keys(UserData.sign_in_passwd)
        driver.find_element(*locators.login_button).click()
        driver.implicitly_wait(2)
        create_order_button = driver.find_element(*locators.create_order_button)

        assert driver.current_url == Urls.main_page and create_order_button.text == 'Оформить заказ'

    def test_login_with_login_link_in_registration_page(self, driver):
        # Проверка успешного входа по ссылке "Войти" на странице регистрации
        driver.get(Urls.registration_page)
        driver.find_element(*locators.login_link_in_registration_page).click()
        driver.find_element(*locators.login_email_input).send_keys(UserData.sign_in_login)
        driver.find_element(*locators.login_passwd_input).send_keys(UserData.sign_in_passwd)
        driver.find_element(*locators.login_button).click()
        driver.implicitly_wait(2)
        create_order_button = driver.find_element(*locators.create_order_button)

        assert driver.current_url == Urls.main_page and create_order_button.text == 'Оформить заказ'

    def test_login_with_login_link_in_forgot_passwd_page(self, driver):
        # Проверка успешного входа по ссылке "Войти" на странице "Восстановить пароль"
        driver.get(Urls.forgot_passwd_page)
        driver.find_element(*locators.login_link_in_forgot_passwd_page).click()
        driver.find_element(*locators.login_email_input).send_keys(UserData.sign_in_login)
        driver.find_element(*locators.login_passwd_input).send_keys(UserData.sign_in_passwd)
        driver.find_element(*locators.login_button).click()
        driver.implicitly_wait(2)
        create_order_button = driver.find_element(*locators.create_order_button)

        assert driver.current_url == Urls.main_page and create_order_button.text == 'Оформить заказ'
