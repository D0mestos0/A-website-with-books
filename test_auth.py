import pytest
from pages.base_page import Base_Page
from pages.auth_page import Auth_Page


class TestAuth:
    @pytest.mark.positive_auth
    def test_positive_login(self, browser):
        base = Base_Page(browser)
        auth = Auth_Page(browser)

        auth.open_auth_page()
        auth.enter_email("test+2679@mail.ru")
        auth.enter_password("Myrasha123456_")
        auth.click_button()
        auth.success_msg()

    @pytest.mark.negative_auth
    @pytest.mark.parametrize(
        "email, password",
        [
            ("test@mail.ru", "Myrasha123456_")
            # ("testmail.ru", "Myrasha123456_")
        ],
    )
    def test_negative_login(self, browser, email, password):
        base = Base_Page(browser)
        auth = Auth_Page(browser)

        auth.open_auth_page()
        auth.enter_email(email)
        auth.enter_password(password)
        auth.click_button()
        auth.error_msg(email, password)


@pytest.fixture(scope="session")
def base_page(browser):
    base = Base_Page(browser)
    yield base 