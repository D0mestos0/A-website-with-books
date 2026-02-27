import pytest
import time
from selenium import webdriver


def log(message):
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] {message} \n")


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    log("Закрываем браузер")
    browser.quit()
