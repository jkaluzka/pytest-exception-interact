"""
pytest configuration file
"""
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def chrome_browser() -> WebDriver:
    options = Options()
    options.headless = True
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    yield browser
    browser.close()


@pytest.fixture(scope="class")
def search_page(chrome_browser: WebDriver) -> WebDriver:
    chrome_browser.get("https://duckduckgo.com")
    return chrome_browser


@pytest.hookimpl(hookwrapper=True)
def pytest_exception_interact(node, call, report):
    """
    Overrides the original hook to save browser state
    in form of a screenshot into the "./errors" directory
    """
    web_driver = None
    for fixture_name in node.fixturenames:
        web_driver = node.funcargs[fixture_name]
        if isinstance(web_driver, WebDriver):
            break
    if not web_driver:
        yield

    _path = "./errors"
    Path(_path).mkdir(parents=True, exist_ok=True)
    name = "-".join(node.nodeid.split("::")[-2:])
    web_driver.save_screenshot(f"{_path}/error_{name}.png")
