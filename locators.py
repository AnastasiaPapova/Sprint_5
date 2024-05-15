from selenium.webdriver.common.by import By

lk_button = By.XPATH, "//p[text()='Личный Кабинет']"  # кнопка "Личный кабинет" на главной странице
registration_link = By.XPATH, "//a[text()='Зарегистрироваться']"  # ссылка регистрации на странице входа в личный кабинет
name_input = By.XPATH, "//fieldset[1]/div/div/input"  # поле ввода email на странице регистрации
email_input = By.XPATH, "//fieldset[2]/div/div/input"  # поле ввода email на странице регистрации
password_input = By.NAME, "Пароль"  # поле ввода email на странице регистрации
registration_button = By.XPATH, "//button[text()='Зарегистрироваться']"  # кнопка "Зарегистрироваться" на странице регистрации
uncorrect_passwd_error = By.XPATH, "//p[text()='Некорректный пароль']"  # ошибка при вводе пароля менее 6 символов
uncorrect_user_error = By.XPATH, ".//p[text()='Такой пользователь уже существует']" # ошибка при вводе некорректного email/существующий email
login_page = By.XPATH, "//h2[text()='Вход']"  # страница авторизации
login_email_input = By.XPATH, "//fieldset[1]/div/div/input" # поле ввода email на странице входа
login_passwd_input = By.XPATH, ".//input[@type='password' and @name='Пароль']" # поле ввода пароля на странице входа
login_button = By.XPATH, "//button[text()='Войти']" # кнопка Войти на странице входа
create_order_button = By.XPATH, "//button[text()='Оформить заказ']" # кнопка "Оформить заказ" на главной странице
login_button_in_main_page = By.XPATH, "//button[text()='Войти в аккаунт']" # кнопка "Войти в аккаунт" на главной странице
login_link_in_registration_page = By.XPATH, "//a[text()='Войти']" # ссылка "Войти" на странице регистрации
login_link_in_forgot_passwd_page = By.XPATH, "//a[text()='Войти']" # ссылка "Войти" на странице "Восстановить пароль"
order_history_button_in_lk = By.XPATH, "//a[text()='История заказов']" # кнопка "История заказов" на странице личного кабинета
constructor_button_in_lk_page = By.XPATH, "//p[text()='Конструктор']" # кнопка "Конструктор" на странице личного кабинета
constructor_page_header = By.XPATH, "//h1[text()='Соберите бургер']" # заголовок на странице конструктора
logo_button = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']" # кнопка логотипа
logout_button = By.XPATH, "//button[text()='Выход']" # кнопка выхода в личном кабинете
burger_buns_section = By.XPATH, "//span[text()='Булки']/parent::*" # кнопка раздела "Булки" на странице конструктора
burger_buns_section_header = By.XPATH, "//h2[text()='Булки']" # заголовок раздела "Булки" на странице конструктора
burger_sauces_section = By.XPATH, "//span[text()='Соусы']/parent::*" # кнопка раздела "Соусы" на странице конструктора
burger_sauces_section_header = By.XPATH, "//h2[text()='Соусы']" # заголовк раздела "Соусы" на странице конструктора
burger_toppings_section = By.XPATH, "//span[text()='Начинки']/parent::*" # кнопка раздела "Начинка" на странице # конструктора
burger_toppings_section_header = By.XPATH, "//h2[text()='Начинки']" # заголовк раздела "Начинка" на странице конструктора

