import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "opera", "MicrosoftEdge"]
    )
    parser.addoption("--executor", default="192.168.1.88")


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")

    if browser == "chrome":
        options = ChromiumOptions()
        options.headless = True
    else:
        options = Options()

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={"browserName": browser, "platformName": "LINUX"}, options=options
    )

    driver.maximize_window()

    def fin():
        time.sleep(1)
        driver.quit()

    request.addfinalizer(fin)

    return driver
