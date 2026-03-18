from pages.base_page import Base_Page
from locators.locators import CataloguePageLocators
from selenium.webdriver.common.keys import Keys
from conftest import log
import time


class Catalogue_page(Base_Page):
    def __init__(self, browser):
        super().__init__(browser)  # обращаемся к родительскому классу

    def open_catalogue_with_products(self, page=3):  # перейти на страницу католога
        log("Браузер открывается")
        url = f"http://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/?page={page}"
        self.open_url(url)

    # нажать на добавить в корзину без перехода на страницу товара
    def add_product_to_basket(self):

        # нужно вычленить название книги
        items = self.find_elements(
            CataloguePageLocators.ITEMS
        )  # это будет список всех class="product_pod"

        current_item = items[8]  # беру конкретно 9 книгу

        # название девятой книги запоминаем
        book = self.find_element_in_element(current_item, CataloguePageLocators.BOOK)
        title_book = book.text

        # нахожу все кнопки добавить в корзину
        buttons_add = self.find_elements(
            CataloguePageLocators.BUTTON_ADD_TO_BASKET
        )  # список из всех этих кнопок
        current_button = buttons_add[8]  # беру конкретно девятую
        current_button.click()

        print(f"В корзину была добавлена книга: {title_book}")
        return title_book

    def get_title_in_the_catalogue(self):
        # нужно вычленить название книги
        items = self.find_elements(
            CataloguePageLocators.ITEMS
        )  # это будет список всех class="product_pod"

        current_item = items[8]  # беру конкретно 9 книгу

        # название девятой книги запоминаем
        book = self.find_element_in_element(current_item, CataloguePageLocators.BOOK)
        title_book = book.text
        print(f"Название книги на странице каталога {title_book}")

        return title_book

    def go_to_product_page(self):
        # нужно вычленить название книги
        items = self.find_elements(
            CataloguePageLocators.ITEMS
        )  # это будет список всех class="product_pod"

        current_item = items[8]  # беру конкретно 9 книгу

        # название девятой книги запоминаем
        book = self.find_element_in_element(current_item, CataloguePageLocators.BOOK)
        book.click()

        self.browser.save_screenshot("product_page.png")

    def go_into_basket(self):  # нажать на кнопку "посмотреть корзину"
        check_basket = self.find_element(CataloguePageLocators.CHECK_BASKET)
        assert check_basket.is_displayed(), "Кнопка 'Посмотреть корзину'не появилась!"
        check_basket.click()

    # проверка строки поиска
    def input_the_title_in_the_search(self, sent_name):
        string_search = self.find_element(CataloguePageLocators.SEARCH_STRING)
        string_search.send_keys(sent_name)
        return sent_name

    # нажать enter на строке поиска
    def click_enter(self):
        string_search = self.find_element(CataloguePageLocators.SEARCH_STRING)
        string_search.send_keys(Keys.ENTER)
