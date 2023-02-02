from pages.elements_page import ElementsPage
from pages.demoqa import DemoQa


def test_navigation(browser):
    nav_page = ElementsPage(browser)
    page_demo = DemoQa(browser)

    page_demo.visit()
    page_demo.btn_elements.click_elem()

    nav_page.refresh()

    browser.refresh()
    browser.back()
    browser.forward()

    assert nav_page.equal_url()
