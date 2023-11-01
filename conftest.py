import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--executor", default="192.168.0.113")


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")

    if browser == "chrome":
        options = ChromiumOptions()
        options.add_argument("headless=new")
        options.set_capability("browserName", browser)
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()
    elif browser == "ie":
        options = IEOptions()
    elif browser == "yandex":
        options = ChromiumOptions()
        options.set_capability("browserVersion", "100")
    else:
        raise ValueError

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        options=options
    )

    driver.maximize_window()

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver
