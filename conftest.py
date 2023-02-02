import pytest
from selenium import webdriver


# Defining fixture for webdriver
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    # setting window size
    driver.set_window_size(width=1000, height=1000)
    yield driver
    driver.quit()
