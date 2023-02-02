from pages.demoqa import DemoQa
from components.components import WebElement


# Checking page url and existence of the element
def test_icon_exist(browser):
    page_obj = DemoQa(browser)

    page_obj.visit()
    page_obj.icon.click_elem()
    # Checking page url
    assert page_obj.equal_url()
    # Checking if element exists
    assert page_obj.icon.exist()

# Just empty line
