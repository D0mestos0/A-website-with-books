from pages.base_page import Base_Page
from pages.catalogue_page import Catalogue_page
from pages.checkout_page import Checkout_Page


class TestCheckout:
    def test_fill_required_fields(self, browser_auth):
        catalogue = Catalogue_page(browser_auth)
        checkout = Checkout_Page(browser_auth)
        base = Base_Page(browser_auth)

        catalogue.open_catalogue_with_products(3)
        catalogue.add_product_to_basket()
        catalogue.arrange_order()
        base.assert_open_required_page_is_open("shipping-address")
        checkout.choose_appeal("Г-жа")
        checkout.enter_name("Клиент")
        checkout.enter_lastname("Клиентова")
        checkout.first_string_address("3 дерево за поворотом рядом с болотом")
        checkout.enter_city("г. Караганда")
        checkout.enter_postcode(39353665)
        checkout.choose_country("Argentina")
        checkout.click_button_continue()
