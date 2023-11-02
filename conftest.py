import random

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--executor", default="192.168.0.105")
    parser.addoption("--platform", default="Windows 10")


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    platform = request.config.getoption("--platform")
    executor_url = f"http://{executor}:4444/wd/hub"

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
    elif browser == "safari":
        options = SafariOptions()
        options.browser_version = '16'
        options.platform_name = 'macOS 12'
        sauce_options = {}
        sauce_options['username'] = 'oauth-m.apelsinov.mail-34d19'
        sauce_options['accessKey'] = '****'
        sauce_options['build'] = "8888"
        sauce_options['name'] = request.node.name
        options.set_capability('sauce:options', sauce_options)
        executor_url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    else:
        raise ValueError

    if browser != "safari":
        options.set_capability("platformName", platform)

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )

    driver.maximize_window()

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver
