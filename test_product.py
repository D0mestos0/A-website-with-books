import pytest
from pages.base_page import Base_Page
from pages.basket_page import Basket_page
from pages.catalogue_page import Catalogue_page
from pages.product_page import Product_page
import time


class Test_Product:
    """Проверяет характеристики товара"""

    def test_check_product(self, browser):
        base = Base_Page(browser)
        catalogue = Catalogue_page(browser)
        basket = Basket_page(browser)
        product = Product_page(browser)

        catalogue.open_catalogue_with_products(3)
        title_book = catalogue.get_title_in_the_catalogue()
        catalogue.go_to_product_page()

        product.get_the_title()
        product.verify_title(title_book)
        product.get_price()
        product.verify_product_is_in_stock()
        product.check_for_a_description()
        product.add_product_to_the_basket()
        product.check_alert_notification()

        catalogue.go_into_basket()

        time.sleep(3)

        base.assert_open_required_page_is_open("basket")

        print("Тест завершен!")
