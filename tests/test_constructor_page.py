import locators
from conftest import driver


class TestBurgerConstructor:

    def test_go_to_burger_sauces_section_in_constructor_page(self, driver):
        # Переход к разделу "Соусы"
        driver.find_element(*locators.BURGER_SAUCES_SECTION).click()
        burger_souces_section_selected = driver.find_element(*locators.BURGER_SAUCES_SECTION_IS_SELECTED)
        assert burger_souces_section_selected.text == 'Соусы'


    def test_go_to_burger_buns_section_in_constructor_page(self, driver):
        # Переход к разделу "Булки"
        driver.find_element(*locators.BURGER_SAUCES_SECTION).click()
        driver.find_element(*locators.BURGER_BUNS_SECTION).click()
        burger_buns_section_selected = driver.find_element(*locators.BURGER_BUNS_SECTION_IS_SELECTED)
        assert burger_buns_section_selected.text == 'Булки'


    def test_go_to_burger_toppings_section_in_constructor_page(self, driver):
        # Переход к разделу "Начинки"
        driver.find_element(*locators.BURGER_TOPPINGS_SECTION).click()
        burger_toppings_section_selected = driver.find_element(*locators.BURGER_TOPPINGS_SECTION_IS_SELECTED)
        assert burger_toppings_section_selected.text == 'Начинки'
