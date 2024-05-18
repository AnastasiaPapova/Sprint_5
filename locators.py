from selenium.webdriver.common.by import By

LK_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"  # кнопка "Личный кабинет" на главной странице
REGISTRATION_LINK = By.XPATH, "//a[text()='Зарегистрироваться']"  # ссылка регистрации на странице входа в личный кабинет
NAME_INPUT = By.XPATH, "//fieldset[1]/div/div/input"  # поле ввода email на странице регистрации
EMAIL_INPUT = By.XPATH, "//fieldset[2]/div/div/input"  # поле ввода email на странице регистрации
PASSWORD_INPUT = By.NAME, "Пароль"  # поле ввода email на странице регистрации
REGISTRATION_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']"  # кнопка "Зарегистрироваться" на странице регистрации
UNCORRECT_PASSWD_ERROR = By.XPATH, "//p[text()='Некорректный пароль']"  # ошибка при вводе пароля менее 6 символов
UNCORRECT_EMAIL_ERROR = By.XPATH, ".//p[text()='Такой пользователь уже существует']" # ошибка при вводе некорректного email/существующий email
LOGIN_PAGE = By.XPATH, "//h2[text()='Вход']"  # страница авторизации
LOGIN_EMAIL_INPUT = By.XPATH, "//fieldset[1]/div/div/input" # поле ввода email на странице входа
LOGIN_PASSWD_INPUT = By.XPATH, ".//input[@type='password' and @name='Пароль']" # поле ввода пароля на странице входа
LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']" # кнопка Войти на странице входа
CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']" # кнопка "Оформить заказ" на главной странице
LOGIN_BUTTON_IN_MAIN_PAGE = By.XPATH, "//button[text()='Войти в аккаунт']" # кнопка "Войти в аккаунт" на главной странице
LOGIN_LINK_IN_REGISTRATION_PAGE = By.XPATH, "//a[text()='Войти']" # ссылка "Войти" на странице регистрации
LOGIN_LINK_IN_FOGOT_PASSWD_PAGE = By.XPATH, "//a[text()='Войти']" # ссылка "Войти" на странице "Восстановить пароль"
ORDER_HISTORY_BUTTON_IN_LK_PAGE = By.XPATH, "//a[text()='История заказов']" # кнопка "История заказов" на странице личного кабинета
CONSTRUCTOR_BUTTON_IN_LK_PAGE = By.XPATH, "//p[text()='Конструктор']" # кнопка "Конструктор" на странице личного кабинета
CONSTRUCTOR_PAGE_HEADER = By.XPATH, "//h1[text()='Соберите бургер']" # заголовок на странице конструктора
LOGO_BUTTON = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']" # кнопка логотипа
LOGOUT_BOTTON = By.XPATH, "//button[text()='Выход']" # кнопка выхода в личном кабинете
BURGER_BUNS_SECTION = By.XPATH, "//span[text()='Булки']/parent::*" # кнопка раздела "Булки" на странице конструктора
BURGER_BUNS_SECTION_IS_SELECTED = By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/child::span[text()='Булки']" # заголовок раздела "Булки" на странице конструктора
BURGER_SAUCES_SECTION = By.XPATH, "//span[text()='Соусы']/parent::*" # кнопка раздела "Соусы" на странице конструктора
BURGER_SAUCES_SECTION_IS_SELECTED = By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/child::span[text()='Соусы']" # заголовк раздела "Соусы" на странице конструктора
BURGER_TOPPINGS_SECTION = By.XPATH, "//span[text()='Начинки']/parent::*" # кнопка раздела "Начинка" на странице # конструктора
BURGER_TOPPINGS_SECTION_IS_SELECTED = By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/child::span[text()='Начинки']" # выбранная секция с названием


