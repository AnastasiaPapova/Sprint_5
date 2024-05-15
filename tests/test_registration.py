import pytest
import locators
from conftest import driver
from main.user_data import UserData
from main.burger_urls import Urls


class TestBurgerRegistration:
    def test_sign_up_successful(self, driver):
        # Проверка успешной регистрации
        driver.get(Urls.registration_page)
        driver.find_element(*locators.name_input).send_keys(UserData.user_name)
        driver.find_element(*locators.email_input).send_keys(UserData.user_email)
        driver.find_element(*locators.password_input).send_keys(UserData.user_passwd)
        driver.find_element(*locators.registration_button).click()
        driver.implicitly_wait(2)
        assert driver.find_element(*locators.login_page).text == 'Вход' and driver.current_url == Urls.login_page

    def test_sign_up_without_name(self, driver):
        # Попытка регистрации без заполненного поля "Имя"
        driver.get(Urls.registration_page)
        driver.find_element(*locators.email_input).send_keys(UserData.user_email)
        driver.find_element(*locators.password_input).send_keys(UserData.user_passwd)
        driver.find_element(*locators.registration_button).click()
        driver.implicitly_wait(2)
        assert driver.current_url == Urls.registration_page

    @pytest.mark.parametrize('fail_passwd', ['1', '123', '5421'])
    def test_sign_up_incorrect_passwd_error(self, driver, fail_passwd):
        # Попытка регистрации с коротким паролем
        driver.get(Urls.registration_page)
        driver.find_element(*locators.name_input).send_keys(UserData.user_name)
        driver.find_element(*locators.email_input).send_keys(UserData.user_email)
        driver.find_element(*locators.password_input).send_keys(fail_passwd)
        driver.find_element(*locators.registration_button).click()
        assert driver.find_element(*locators.uncorrect_passwd_error).text == 'Некорректный пароль'

    @pytest.mark.parametrize('uncorrect_email', ['eg@.ru', 'my@email.ru'])
    def test_sign_up_incorrect_email_error(self, driver, uncorrect_email):
        # Попытка регистрации с некорректным email
        driver.get(Urls.registration_page)
        driver.find_element(*locators.name_input).send_keys(UserData.user_name)
        driver.find_element(*locators.email_input).send_keys(uncorrect_email)
        driver.find_element(*locators.password_input).send_keys(UserData.user_passwd)
        driver.find_element(*locators.registration_button).click()
        driver.implicitly_wait(2)
        assert driver.find_element(*locators.uncorrect_user_error).text == 'Такой пользователь уже существует'
