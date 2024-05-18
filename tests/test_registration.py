import pytest
import locators
from conftest import driver
from main.user_data import UserData
from main.burger_urls import Urls


class TestBurgerRegistration:
    def test_sign_up_successful(self, driver):
        # Проверка успешной регистрации
        driver.get(Urls.REGISTRATION_PAGE)
        driver.find_element(*locators.NAME_INPUT).send_keys(UserData.USER_NAME)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(UserData.user_email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(UserData.USER_PASSWD)
        driver.find_element(*locators.REGISTRATION_BUTTON).click()
        driver.implicitly_wait(2)
        assert driver.find_element(*locators.LOGIN_PAGE).text == 'Вход' and driver.current_url == Urls.LOGIN_PAGE

    def test_sign_up_without_name(self, driver):
        # Попытка регистрации без заполненного поля "Имя"
        driver.get(Urls.REGISTRATION_PAGE)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(UserData.user_email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(UserData.USER_PASSWD)
        driver.find_element(*locators.REGISTRATION_BUTTON).click()
        driver.implicitly_wait(2)
        assert driver.current_url == Urls.REGISTRATION_PAGE

    @pytest.mark.parametrize('fail_passwd', ['1', '123', '5421'])
    def test_sign_up_incorrect_passwd_error(self, driver, fail_passwd):
        # Попытка регистрации с коротким паролем
        driver.get(Urls.REGISTRATION_PAGE)
        driver.find_element(*locators.NAME_INPUT).send_keys(UserData.USER_NAME)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(UserData.user_email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(fail_passwd)
        driver.find_element(*locators.REGISTRATION_BUTTON).click()
        assert driver.find_element(*locators.UNCORRECT_PASSWD_ERROR).text == 'Некорректный пароль'

    @pytest.mark.parametrize('uncorrect_email', ['eg@.ru', 'my@email.ru'])
    def test_sign_up_incorrect_email_error(self, driver, uncorrect_email):
        # Попытка регистрации с некорректным email
        driver.get(Urls.REGISTRATION_PAGE)
        driver.find_element(*locators.NAME_INPUT).send_keys(UserData.USER_NAME)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(uncorrect_email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(UserData.USER_PASSWD)
        driver.find_element(*locators.REGISTRATION_BUTTON).click()
        driver.implicitly_wait(2)
        assert driver.find_element(*locators.UNCORRECT_EMAIL_ERROR).text == 'Такой пользователь уже существует'
