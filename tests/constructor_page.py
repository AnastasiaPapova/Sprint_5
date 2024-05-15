import locators
from conftest import driver


class TestBurgerConstructor:

    def test_go_to_burger_sauces_section_in_constructor_page(self, driver):
        # Переход к разделу "Соусы"
        driver.find_element(*locators.burger_sauces_section).click()
        burger_souces_section = driver.find_element(*locators.burger_sauces_section_header)
        assert burger_souces_section.text == 'Соусы'

    def test_go_to_burger_buns_section_in_constructor_page(self, driver):
        # Переход к разделу "Булки"
        driver.find_element(*locators.burger_sauces_section).click()
        driver.find_element(*locators.burger_buns_section).click()
        burger_buns_section = driver.find_element(*locators.burger_buns_section_header)
        assert burger_buns_section.text == 'Булки'

    def test_go_to_burger_toppings_section_in_constructor_page(self, driver):
        # Переход к разделу "Начинки"
        driver.find_element(*locators.burger_toppings_section).click()
        burger_toppings_section = driver.find_element(*locators.burger_toppings_section_header)
        assert burger_toppings_section.text == 'Начинки'
