from selenium.webdriver.common.by import By


class CataloguePageLocators:
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[text()='Добавить в корзину']")
    CHECK_BASKET = (By.XPATH, "//a[text()='Посмотреть корзину']")
    ITEMS = (By.CSS_SELECTOR, ".product_pod")
    BOOK = (By.CSS_SELECTOR, "h3 a")
    SEARCH_STRING = (By.CSS_SELECTOR, "#id_q")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BOOK = (By.CSS_SELECTOR, "h3 a")
    DELETE_BUTTON = (By.XPATH, "//a[@data-behaviours='remove']")
    TR_TAG = (By.TAG_NAME, "tr")
    PRICE = (By.CSS_SELECTOR, "td h3")


class ProductPageLocators:
    PRODUCT_MAIN = (By.CSS_SELECTOR, ".col-sm-6.product_main")
    TITLE = (By.TAG_NAME, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div p")
    ICON_OK = (By.CSS_SELECTOR, "div p.instock.availability")
    DESCRIPTION = (By.CSS_SELECTOR, "article p")
    BUTTON_BASKET = (By.XPATH, "//button[text()='Добавить в корзину']")
    ALERTS = (By.CSS_SELECTOR, "div.alertinner")


class SearchPageLocators:
    FOUND_ELEMENT = (By.CSS_SELECTOR, "div form strong")
    TITLE = (By.CSS_SELECTOR, "article h3 a")
    STATUS_OK = (By.CLASS_NAME, "icon-ok")
    STATUS_REMOVE = (By.CSS_SELECTOR, ".icon-remove")
    ABOUT_PRODUCT = (By.CSS_SELECTOR, ".product_price")
    BASKET_TRUE = (By.XPATH, "//button[text()='Добавить в корзину']")
    BASKET_FALSE = (By.XPATH, "//span[text()='Добавить в корзину']")


class RegisterPageLocators:
    EMAIL = (By.XPATH, "//input[@name='registration-email']")
    PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    REPEAT_PASSWORD = (By.XPATH, "//input[@name='registration-password2']")
    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
    SUCCESS_MSG = (By.XPATH, "//div[@class='alertinner wicon']")
    ERROR = (By.CSS_SELECTOR, ".alert.alert-danger")
    ERROR_BLOCKS = (By.CSS_SELECTOR, ".error-block")


class AuthPageLocators:
    EMAIL = (By.XPATH, "//input[@name='login-username']")
    PASSWORD = (By.XPATH, "//input[@name='login-password']")
    BUTTON_LOGIN = (By.XPATH, "//button[@name='login_submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alertinner.wicon")
    ERRORS = (By.CSS_SELECTOR, ".alert.alert-danger")
