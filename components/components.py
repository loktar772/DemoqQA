from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time


# Creating basic methods for working with page elements
class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    # Creating method for elements click
    def click_elem(self):
        self.find_element().click()

    # Creating method for finding elements by CSS Selector
    def find_element(self):
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    # Creating method for check if element exist
    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    # Creating method for getting element text
    def get_text(self):
        return str(self.find_element().text)

    # Creating method for check if element displayed
    def visible(self):
        return self.find_element().is_displayed()

    # Creating method for checking if  url of the current page is equal to given
    def not_visible(self, time_wait=2):
        try:
            WebDriverWait(self.driver, time_wait).until_not(ec.invisibility_of_element((By.CSS_SELECTOR, self.locator)))
            return False
        except TimeoutException:
            return True

    def check_count_elements(self, count: int):
        if len(self.find_elements()) == count:
            return True
        return False
# Just empty line
