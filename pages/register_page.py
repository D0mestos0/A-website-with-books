from pages.base_page import Base_Page
from locators.locators import RegisterPageLocators


class Register_Page(Base_Page):
    def __init__(self, browser):
        super().__init__(browser)

    def open_register_page(self):
        url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.open_url(url)

    def enter_email(self, email):
        email_field = self.find_element(RegisterPageLocators.EMAIL)
        email_field.send_keys(email)
        self.log("Почта успешно вставлена в поле")

    def enter_password(self, password):
        password_field = self.find_element(RegisterPageLocators.PASSWORD)
        password_field.send_keys(password)
        self.log("Пароль успешно вставлен в поле")

    def enter_password_repeat(self, repeat_password):
        rep_password = self.find_element(RegisterPageLocators.REPEAT_PASSWORD)
        rep_password.send_keys(repeat_password)
        self.log("Пароль успешно повторился")

    def click_button(self):
        button = self.find_element(RegisterPageLocators.BUTTON_REGISTER)
        button.click()
        self.log("Кнопка регистрации успешно нажата!")

    def success_msg(self):
        self.browser.save_screenshot("register_success.png")
        msg = self.find_element(RegisterPageLocators.SUCCESS_MSG)
        assert (
            "Спасибо за регистрацию!" in msg.text
        ), f"Ожидали сообщение об успешной регистрации, а получили {msg}"
        self.log("Регистрация прошла успешно!")

    def error_msg(self, email, password, repeat_password):

        self.log("Зашла в метод ошибок")

        try:
            self.log("Пытаюсь обнаружить ошибку на странице")
            error = self.find_element(RegisterPageLocators.ERROR)
            password_field = self.find_element(RegisterPageLocators.PASSWORD)

            if error.is_displayed():
                self.log("Обнаружена ошибка от сайта!")
                self.scroll(error)
                self.browser.save_screenshot("error.png")
                self.log(f"{error.text}")

                error_blocks = self.find_elements(RegisterPageLocators.ERROR_BLOCKS)

                for error in error_blocks:
                    self.log(f"{error.text}")

                self.log(
                    f"Были использованы следующие данные при регистрации: {email}, {password}, {repeat_password}"
                )
            else:
                self.log("Ошибки от сайта не было, проверяю дальше")
        except:
            self.log("Проверяю наличие HTML5 ошибки!")
            list_fields = [
                ("Email", RegisterPageLocators.EMAIL),
                ("Password", RegisterPageLocators.PASSWORD),
                ("Repeat_password", RegisterPageLocators.REPEAT_PASSWORD),
            ]

            for field, locator in list_fields:
                field_name = self.find_element(locator)
                validation_error = field_name.get_attribute("validationMessage")

                if validation_error:
                    self.log("HTML5 валидация!")
                    self.scroll(field_name)
                    self.browser.save_screenshot("html5.png")
                    self.log(f"Поле: {field}, сообщение {validation_error}")
                    self.log(
                        f"Были использованые следующие данные при регистрации: {email}, {password}, {repeat_password}"
                    )
