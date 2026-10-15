
import pytest  # pytest ke tools import karta hai.
from selenium import webdriver # Selenium browser control karne ke liye import hota hai.


@pytest.fixture  # Reusable browser setup banata hai.
def driver():
    # Launch Chrome using Selenium WebDriver.
    browser = webdriver.Chrome()

    # Maximize the browser window.
    browser.maximize_window()

    # Make the browser available to the test.
    yield browser

    # Close the browser after the test finishes.
    browser.quit()
