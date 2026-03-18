from pages.base_page import Base_Page
from locators.locators import CheckOutLocators
from selenium.webdriver.support.ui import Select


class Checkout_Page(Base_Page):
    def __init__(self, browser):
        super().__init__(browser)

    def choose_appeal(self, appeal):

        # это просто веб элемент поля селекта
        dropdown_element = self.find_element(CheckOutLocators.DROPDOWN_ELEMENT)

        # мне нужно создать объект класса Select, чтобы пользоваться методами этого класса
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(appeal)
        self.log(f"Выбрано следующее обращение - {appeal}")

    def enter_name(self, name):
        name_field = self.find_element(CheckOutLocators.NAME_FIELD)
        name_field.send_keys(name)
        self.log(f"В поле имя вставлено имя - {name}")

    def enter_lastname(self, lastname):
        lastname_field = self.find_element(CheckOutLocators.LAST_NAME)
        lastname_field.send_keys(lastname)
        self.log(f"В поле фамилия вставлено - {lastname}")

    def first_string_address(self, address):
        address_field = self.find_element(CheckOutLocators.FIRST_ADDRESS)
        address_field.send_keys(address)
        self.log(f"В поле адрес указан следующий адрес - {address}")

    def enter_city(self, city):
        city_field = self.find_element(CheckOutLocators.CITY)
        city_field.send_keys(city)
        self.log(f"В поле города - {city}")

    def enter_postcode(self, postcode):
        postcode_field = self.find_element(CheckOutLocators.POSTCODE)
        postcode_field.send_keys(postcode)
        self.log(f"В поле индекса - {postcode}")

    def choose_country(self, country):
        dropdown_element = self.find_element(CheckOutLocators.COUNTRY_DROPDOWN)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(country)
        self.log(f"Выбрана следующая страна - {country}")

    def click_button_continue(self):
        button = self.find_element(CheckOutLocators.BUTTON)
        button.click()
        self.log("Кнопка 'Продолжить' была нажата! ")
