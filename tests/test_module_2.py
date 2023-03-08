from selenium.webdriver.common.by import By


def test_google_0(remote):
    remote.get("https://google.ru")
    remote.find_element(By.NAME, "q")
    assert remote.title == "Google"


def test_yandex_0(remote):
    remote.get("https://ya.ru")
    remote.find_element(By.NAME, "text")
    assert remote.title == "Яндекс"


def test_google_1(remote):
    remote.get("https://google.ru")
    remote.find_element(By.NAME, "q")
    assert remote.title == "Google"


def test_yandex_1(remote):
    remote.get("https://ya.ru")
    remote.find_element(By.NAME, "text")
    assert remote.title == "Яндекс"


def test_google_2(remote):
    remote.get("https://google.ru")
    remote.find_element(By.NAME, "q")
    assert remote.title == "Google"


def test_yandex_2(remote):
    remote.get("https://ya.ru")
    remote.find_element(By.NAME, "text")
    assert remote.title == "Яндекс"
