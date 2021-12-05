import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "opera", "MicrosoftEdge"]
    )
    parser.addoption("--executor", default="192.168.1.88")


@pytest.fixture
def firefox(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def chrome(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={"browserName": browser}
    )
    driver.implicitly_wait(2)
    driver.maximize_window()

    request.addfinalizer(driver.quit)

    return driver
