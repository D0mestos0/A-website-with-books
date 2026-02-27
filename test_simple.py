def test_google(browser):  # ← browser берется из conftest.py
    browser.get("https://google.com")
    print("✅ Тест выполнился")
    assert True
