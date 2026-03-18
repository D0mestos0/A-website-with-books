import pytest
import time
from pages.base_page import Base_Page
from pages.register_page import Register_Page


@pytest.mark.auth
class TestRegister:

    @pytest.mark.positive
    def test_positive_register(self, browser):
        base = Base_Page(browser)
        register = Register_Page(browser)

        register.open_register_page()
        register.enter_email("test+2679@mail.ru")
        register.enter_password("Myrasha123456_")
        register.enter_password_repeat("Myrasha123456_")
        register.click_button()
        time.sleep(2)
        register.success_msg()

    @pytest.mark.negative
    @pytest.mark.parametrize(
        "email, password, repeat_password",
        [
            # проверка поля email
            # ("test@.mail.ru", "Myrasha123456_", "Myrasha123456_"),
            ("test+2679@mail.ru", "Myrasha123456_", "Myrasha123456_")
            # ("test@mail,ru", "Myrasha123456_", "Myrasha123456_"),
            # ("test#mail.ru", "Myrasha123456_", "Myrasha123456_"),
            # проверка поля password
            # ("test@mail.ru", "qwertyui", "qwertyui"),
            # ("test@mail.ru", "Qw", "Qw"),
            # проверка поля rep_password
            # ("test@mail.ru", "Myrasha123456_", "t"),
        ],
    )
    def test_negative_register(self, browser, email, password, repeat_password):
        base = Base_Page(browser)
        register = Register_Page(browser)

        register.open_register_page()
        register.enter_email(email)
        register.enter_password(password)
        register.enter_password_repeat(repeat_password)
        register.click_button()
        time.sleep(1)
        register.error_msg(email, password, repeat_password)
