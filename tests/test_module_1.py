import time

from selenium.webdriver.common.by import By


def test_google_0(remote):
    remote.get("https://google.ru")
    remote.find_element(By.NAME, "q")
    assert remote.title == "Google"


def test_yandex_0(remote):
    remote.get("https://ya.ru")
    remote.find_element(value="text")
    remote.find_element(By.CSS_SELECTOR, "a[title='Яндекс']")
    assert remote.title == "Яндекс"


def test_avito_0(remote):
    remote.get("https://avito.ru")
    remote.find_element(value="category")
    remote.find_element(By.CSS_SELECTOR, "[data-marker='search-form/suggest']")
    assert "Авито" in remote.title
