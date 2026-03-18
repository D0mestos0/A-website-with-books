import pytest
from pages.catalogue_page import Catalogue_page
from pages.base_page import Base_Page
from pages.search_page import Search_Page


class Test_Search:
    def test_search_string(self, browser):

        catalogue = Catalogue_page(browser)
        search = Search_Page(browser)

        catalogue.open_catalogue_with_products(3)
        sent_name = catalogue.input_the_title_in_the_search(
            "Hackers & painters"
        )  # Hackers & painters
        catalogue.click_enter()

        search.check_result()
        search.comparing_the_names(sent_name)
        search.get_status_of_product()
        search.check_basket()
