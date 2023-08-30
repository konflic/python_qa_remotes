import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        # choices=["chrome", "firefox", "MicrosoftEdge"]
    )
    parser.addoption("--executor", default="127.0.0.1")


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")

    if browser == "chrome":
        options = ChromiumOptions()
        options.add_argument("headless=new")
        options.set_capability("browserName", browser)

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        options=options
    )

    driver.maximize_window()

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver
