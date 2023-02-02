from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


# Checking for url of the page is equal to given
def test_go_to_page_elements(browser):
    go_to_elements = DemoQa(browser)
    page_elements = ElementsPage(browser)

    go_to_elements.visit()
    assert go_to_elements.equal_url()
    go_to_elements.btn_elements.click_elem()
    assert page_elements.equal_url()

# Just empty line
