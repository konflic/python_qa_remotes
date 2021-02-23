import time


def test_google_0(remote):
    remote.get("https://google.ru")
    remote.find_element_by_name("q")
    assert remote.title == "Google"
    time.sleep(1)


def test_yandex_0(remote):
    remote.get("https://ya.ru")
    remote.find_element_by_id("text")
    remote.find_element_by_css_selector("a[title='Яндекс']")
    assert remote.title == "Яндекс"
    time.sleep(1)


def test_avito_0(remote):
    remote.get("https://avito.ru")
    remote.find_element_by_id("category")
    remote.find_element_by_id("search")
    assert "Авито" in remote.title
    time.sleep(1)


def test_google_1(remote):
    remote.get("https://google.ru")
    remote.find_element_by_name("q")
    assert remote.title == "Google"
    time.sleep(1)


def test_yandex_1(remote):
    remote.get("https://ya.ru")
    remote.find_element_by_id("text")
    remote.find_element_by_css_selector("a[title='Яндекс']")
    assert remote.title == "Яндекс"
    time.sleep(1)


def test_avito_1(remote):
    remote.get("https://avito.ru")
    remote.find_element_by_id("category")
    remote.find_element_by_id("search")
    assert "Авито" in remote.title
    time.sleep(1)
