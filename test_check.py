# test_ только в ТЕСТАХ!

import pytest
from pages.catalogue_page import Catalogue_page
from pages.basket_page import Basket_page
from pages.base_page import Base_Page


class Test_add_product_to_basket:
    def test_add_product(self, browser):  # <- browser из conftest!
        """Сценарий добавления товара в корзину и проверка наличия его там"""

        catalogue = Catalogue_page(browser)
        basket = Basket_page(browser)

        catalogue.open_catalogue_with_products(3)
        print("✅ Открыли каталог")

        title_book = catalogue.add_product_to_basket()
        print(f"\n📖 Добавили товар: '{title_book}'")

        catalogue.go_into_basket()
        print("✅ Перешли в корзину")

        assert "basket" in browser.current_url, "Страница с корзиной не открылась!"
        print("Страница с корзиной успешно открыта!")

        basket.verify_item_in_the_basket(title_book)

        browser.save_screenshot("basket.png")
