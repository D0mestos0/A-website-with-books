"""Удаление товара из корзины"""

import pytest
from pages.base_page import Base_Page
from pages.basket_page import Basket_page
from pages.catalogue_page import Catalogue_page


class Test_delete_the_product:
    @pytest.mark.xfail(reason="Кнопка удаления не работает!")
    def test_delete_the_book_from_basket(self, browser):  # В классе ВСЕГДА нужен self первым параметром!
        catalogue = Catalogue_page(browser)
        basket = Basket_page(browser)

        catalogue.open_catalogue_with_products(3)
        catalogue.add_product_to_basket()
        catalogue.go_into_basket()

        basket.delete_the_product()
        print("Тест успешно завершен!")
