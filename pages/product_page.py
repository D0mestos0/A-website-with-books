from pages.base_page import Base_Page
from pages.catalogue_page import Catalogue_page
from locators.locators import ProductPageLocators


class Product_page(Base_Page):
    def __init__(self, browser):
        super().__init__(browser)

    def get_the_title(self):
        product_main = self.find_element(ProductPageLocators.PRODUCT_MAIN)
        title = self.find_element_in_element(product_main, ProductPageLocators.TITLE)
        title_text = title.text
        print(f"Название книги на ее странице {title_text}")
        return title_text

    def verify_title(self, expected_title):
        title_on_the_product_page = self.get_the_title()
        expected_title_fix = expected_title.replace("...", "").strip()
        assert (
            expected_title_fix in title_on_the_product_page
        ), f"На странице товара название {title_on_the_product_page}, но нажимали мы на товар {expected_title}"

    def get_price(self):
        product_main = self.find_element(ProductPageLocators.PRODUCT_MAIN)
        price = self.find_element_in_element(
            product_main, ProductPageLocators.PRICE_PRODUCT
        )
        price_text = price.text
        print(f"Цена товара {price_text}")
        return price_text

    def verify_product_is_in_stock(self):
        product_main = self.find_element(ProductPageLocators.PRODUCT_MAIN)
        true_in_the_basket = self.find_element_in_element(
            product_main, ProductPageLocators.ICON_OK
        )
        true_in_the_basket_text = true_in_the_basket.text

        try:
            if "На складе" in true_in_the_basket_text:
                print(f"Товар на складе есть - {true_in_the_basket_text}")
            elif "Недоступно" in true_in_the_basket_text:
                print(f"Товара на складе нет - {true_in_the_basket_text}")
            else:
                print("Не найдено информации о наличии или об отсутствии товара")
        except Exception as e:
            print(f"Ошибка: {e}")

    def check_for_a_description(self):
        description = self.find_element(ProductPageLocators.DESCRIPTION)
        description_text = description.text
        return description_text

    def add_product_to_the_basket(self):
        button = self.find_element(ProductPageLocators.BUTTON_BASKET)
        button.click()

    def check_alert_notification(self):
        # это список алертов
        alerts = self.find_elements(ProductPageLocators.ALERTS)
        alert_message = alerts[0]
        assert alert_message.is_displayed(), f"Сообщение о добавлении товара в корзину не было найдено. Было получено {alert_message.text}"
        print(f"{alert_message.text}")
        return alert_message.text
