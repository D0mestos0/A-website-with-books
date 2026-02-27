from pages.base_page import Base_Page
from locators.locators import AuthPageLocators


class Auth_Page(Base_Page):
    def __init__(self, browser):
        super().__init__(browser)

    def open_auth_page(self):
        url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.open_url(url)

    def enter_email(self, email):
        email_field = self.find_element(AuthPageLocators.EMAIL)
        email_field.send_keys(email)
        self.log("Почта добавлена в поле")

    def enter_password(self, password):
        password_field = self.find_element(AuthPageLocators.PASSWORD)
        password_field.send_keys(password)
        self.log("Пароль добавлен в поле")

    def click_button(self):
        button = self.find_element(AuthPageLocators.BUTTON_LOGIN)
        button.click()
        self.log("Кнопка 'Войти' нажата")

    def success_msg(self):
        msg = self.find_element(AuthPageLocators.SUCCESS_MSG)
        self.browser.save_screenshot("success_login.png")
        assert "Рады видеть вас снова" in msg.text, f"Вход в аккаунт не был выполнен!"
        self.log("Вход успешно выполнен!")

    def error_msg(self, email, password):
        self.log("Пытаюсь найти какую-либо ошибку!")

        try:
            errors = self.find_elements(AuthPageLocators.ERRORS)
            self.log("Ищу ошибку сайта")

            if len(errors) > 0:
                self.log("Найдены ошибки от сайта!")
                self.scroll(errors[0])
                self.browser.save_screenshot("errors.png")

                for error in errors:
                    self.log(f"Ошибка - {error.text}")

                self.log(
                    f"Были использованые следующие данные при регистрации: {email}, {password}"
                )
            else:
                self.log("Ошибки сайта не были обнаружены!")
        except:
            self.log("Проверяю наличие HTML5 ошибки!")
            params = [
                ("Email", AuthPageLocators.EMAIL),
                ("Password", AuthPageLocators.PASSWORD),
            ]

            for field, locator in params:
                field_name = self.find_element(locator)
                validation_msg = field_name.get_attribute("validationMessage")

                if validation_msg:
                    self.log("Обнаружена HTML5 валидация!")
                    self.scroll(field_name)
                    self.browser.save_screenshot("html5.png")
                    self.log(f"Поле: {field}, сообщение {validation_msg}")
                    self.log(
                        f"Были использованые следующие данные при регистрации: {email}, {password}"
                    )
