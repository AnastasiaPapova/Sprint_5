import locators
from conftest import driver
from conftest import login
from main.burger_urls import Urls
from main.user_data import UserData


class TestBurgerLogin:
    def test_login_successfull(self, driver, login):
        # Проверка успешного входа
        create_order_button = driver.find_element(*locators.CREATE_ORDER_BUTTON)
        assert driver.current_url == Urls.BASE_URL and create_order_button.text == 'Оформить заказ'


    def test_login_with_lk_button(self, driver):
        # Проверка успешного входа по кнопке личного кабинета
        driver.get(Urls.BASE_URL)
        driver.find_element(*locators.LK_BUTTON).click()
        driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(UserData.SIGN_IN_LOGIN)
        driver.find_element(*locators.LOGIN_PASSWD_INPUT).send_keys(UserData.SIGN_IN_PASSWD)
        driver.find_element(*locators.LOGIN_BUTTON).click()
        driver.implicitly_wait(2)
        create_order_button = driver.find_element(*locators.CREATE_ORDER_BUTTON)
        assert driver.current_url == Urls.BASE_URL and create_order_button.text == 'Оформить заказ'


    def test_login_with_login_button_in_main_page(self, driver):
        # Проверка успешного входа по кнопке "Войти в аккаунт" на главной странице
        driver.get(Urls.BASE_URL)
        driver.find_element(*locators.LOGIN_BUTTON_IN_MAIN_PAGE).click()
        driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(UserData.SIGN_IN_LOGIN)
        driver.find_element(*locators.LOGIN_PASSWD_INPUT).send_keys(UserData.SIGN_IN_PASSWD)
        driver.find_element(*locators.LOGIN_BUTTON).click()
        driver.implicitly_wait(2)
        create_order_button = driver.find_element(*locators.CREATE_ORDER_BUTTON)
        assert driver.current_url == Urls.BASE_URL and create_order_button.text == 'Оформить заказ'


    def test_login_with_login_link_in_registration_page(self, driver):
        # Проверка успешного входа по ссылке "Войти" на странице регистрации
        driver.get(Urls.REGISTRATION_PAGE)
        driver.find_element(*locators.LOGIN_LINK_IN_REGISTRATION_PAGE).click()
        driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(UserData.SIGN_IN_LOGIN)
        driver.find_element(*locators.LOGIN_PASSWD_INPUT).send_keys(UserData.SIGN_IN_PASSWD)
        driver.find_element(*locators.LOGIN_BUTTON).click()
        driver.implicitly_wait(2)
        create_order_button = driver.find_element(*locators.CREATE_ORDER_BUTTON)
        assert driver.current_url == Urls.BASE_URL and create_order_button.text == 'Оформить заказ'


    def test_login_with_login_link_in_forgot_passwd_page(self, driver):
        # Проверка успешного входа по ссылке "Войти" на странице "Восстановить пароль"
        driver.get(Urls.FORGOT_PASSWD_PAGE)
        driver.find_element(*locators.LOGIN_LINK_IN_FOGOT_PASSWD_PAGE).click()
        driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(UserData.SIGN_IN_LOGIN)
        driver.find_element(*locators.LOGIN_PASSWD_INPUT).send_keys(UserData.SIGN_IN_PASSWD)
        driver.find_element(*locators.LOGIN_BUTTON).click()
        driver.implicitly_wait(2)
        create_order_button = driver.find_element(*locators.CREATE_ORDER_BUTTON)
        assert driver.current_url == Urls.BASE_URL and create_order_button.text == 'Оформить заказ'
