from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Base_Page:
    """Базовый класс для всех страниц"""

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15)

    def log(self, message):
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {message} \n")

    def open_url(self, url):
        """Открыть любой URL"""
        self.log("Браузер открывается")
        self.browser.get(url)
        self.log(f"Открыта страница: {url}")

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.browser.find_elements(*locator)

    def find_element_in_element(self, parent_element, locator):
        return parent_element.find_element(locator[0], locator[1])

    def click_element(self, locator):
        """Клик по кнопке"""
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()
        print(
            f"Кликнули на элемент: {locator[1]}"
        )  # locator - это кортеж, по сути мы выбираем второй аргумент (By.CSS_SELECTOR, "h3 a")

    def get_text_of_element(self, locator):
        """Получаем текст элемента"""
        element = self.find_element(locator)
        return element.text

    def assert_open_required_page_is_open(self, expected_part):
        print(f"Ищем в URL: {expected_part}")
        print(f"Текущий URL: {self.browser.current_url}")
        self.browser.save_screenshot("current_url.png")
        assert (
            expected_part in self.browser.current_url
        ), f"URL не содержит '{expected_part}'!"

    def scroll(self, element, position="center"):
        """
        Как проскроллить к элементу

        :position: start, center, end
        """
        self.browser.execute_script(
            f"arguments[0].scrollIntoView({{block: '{position}'}});", element
        )
