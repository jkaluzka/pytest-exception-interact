"""
pytest configuration file
"""
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
