from pages.base_page import Base_Page
from pages.catalogue_page import Catalogue_page
from locators.locators import SearchPageLocators
import time


class Search_Page(Base_Page):

    # Вызывается АВТОМАТИЧЕСКИ при создании объекта (в тестах)
    def __init__(self, browser):
        super().__init__(browser)

    def check_result(self):
        self.log("Ищем результаты")
        time.sleep(1)
        found = self.find_element(SearchPageLocators.FOUND_ELEMENT)
        found_text = found.text
        self.log(f"Найдено {found_text} результат (-ов)")

    def comparing_the_names(self, sent_title):
        catalogue = Catalogue_page(self.browser)
        self.log("Находим название книги после запроса поиска")

        # если будет найден список книг
        try:
            title_after_search = catalogue.get_title_in_the_catalogue()
            title_after_search_text = title_after_search.text
            self.log(f"Нашли название - {title_after_search_text}")
        except:
            # если будет не список, а одна книга
            title_after_search = self.find_element(SearchPageLocators.TITLE)
            title_after_search_text = title_after_search.text
            self.log(f"Нашли название - {title_after_search_text}")

        title_after_search_text_new = title_after_search_text.replace("...", "")

        self.log("Сравниваем названия введенной и полученной книг")
        self.browser.save_screenshot("search_page.png")
        assert (
            title_after_search_text_new in sent_title
        ), f"Искали книгу {sent_title}, а нашли {title_after_search_text_new}"
        self.log("Названия успешно совпадают! Поиск работает!")

    def get_status_of_product(self):
        self.log("Проверяю наличие или отсутствие книги на складе")

        try:
            status = self.find_element(SearchPageLocators.STATUS_OK)
            self.log(f"Книга есть на складе!")
        except:
            status = self.find_element(SearchPageLocators.STATUS_REMOVE)
            self.log(f"Книги на складе нет!")

    def check_basket(self):
        self.log("Проверяю доступность кнопки 'Добавить в корзину'")
        about_product = self.find_element(SearchPageLocators.ABOUT_PRODUCT)
        text = about_product.text

        if "На складе" in text:
            self.browser.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", about_product
            )
            self.browser.save_screenshot("icon-ok.png")
            self.log("Книгу можно добавить в корзину!")
            basket = self.find_element(SearchPageLocators.BASKET_TRUE)
            basket.click()
            self.log("Книга добавлена в корзину!")
        else:

            self.browser.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", about_product
            )
            self.browser.save_screenshot("icon-remove.png")
            basket = self.find_element(SearchPageLocators.BASKET_FALSE)

            basket_class = basket.get_attribute("class")  # Возвращает содержимое класса

            if "disabled" in basket_class:
                self.log(
                    "Так как книги нет на складе, то ее нельзя добавить в корзину!"
                )
