"""Что здесь происходит:
- подтверждение наличия товара в корзине
"""

import time
from pages.base_page import Base_Page
from locators.locators import BasketPageLocators


class Basket_page(Base_Page):
    def __init__(self, browser):
        super().__init__(browser)

    def open_basket(self):
        url = "https://selenium1py.pythonanywhere.com/ru/basket/"
        self.open_url(url)

    def verify_item_in_the_basket(self, expected_title):
        """Проверить что товар есть в корзине"""
        basket_items = self.find_elements(
            BasketPageLocators.BASKET_ITEMS
        )  # это список class="basket-items"

        found = False

        for item in basket_items:
            book = self.find_element_in_element(item, BasketPageLocators.BOOK)
            book_title = book.text
            expected_clean = expected_title.replace("...", "")

            if expected_clean in book_title:
                found = True
                break

        time.sleep(5)
        assert (
            found
        ), f"Ожидали добавления в корзину {expected_title}, а добавили {book_title}"
        self.browser.execute_script("window.scrollBy(0, 150);")
        self.browser.save_screenshot("books.png")

        # found = False

        # for item in basket_items:
        # book = self.find_element_in_element(basket_items, BasketPageLocators.BOOK)
        # book_title = book.text

        # if book_title == expected_title:
        # found = True
        # break

    def get_price(self):
        """Получаю стоимость корзины"""
        # сначала получаю стоимость корзины ДО удаления (там такая же пляска элемент внутри элемента)
        tr_elements = self.find_elements(
            BasketPageLocators.TR_TAG
        )  # это будет список из tr

        try:
            for tr in tr_elements:
                text = tr.text  # получаю текст
                print(f"TR текст: {text}")
                if "Всего" in text and "в корзине" not in text:
                    print("Нашли TR с 'Всего'!")
                    price = self.find_element_in_element(tr, BasketPageLocators.PRICE)
                    print(f"Стоимость корзины: {price.text}")
                    return price.text

            # Если не нашли TR с "Всего" - корзина пустая
            # print("Корзина пустая (не нашли TR с 'Всего')")
            # return "0"
        except Exception as e:
            print(f"Ошибка при получении цены {e}")
            return "0"

    def delete_the_product(self):
        """Удаление товара из корзины на кнопку УДАЛИТЬ"""

        old_price = self.get_price()
        print(f"Цена ДО удаления: {old_price}")

        # нахожу кнопку удаления
        delete_button = self.find_element(BasketPageLocators.DELETE_BUTTON)
        delete_button.click()
        print("🗑️ Кликнули на 'Удалить'")

        time.sleep(2)

        # после удаления снова получаю по идее обновленную цену
        new_price = self.get_price()
        print(f"💰 Цена ПОСЛЕ удаления: {new_price}")
        assert (
            old_price != new_price
        ), f"Стоимость корзины не поменялась! Было: {old_price}, Стало: {new_price}"

        print(f"✅ Товар удален! Было: {old_price}, Стало: {new_price}")
