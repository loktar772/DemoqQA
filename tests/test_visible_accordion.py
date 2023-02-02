from pages.accordion_page import AccordionPage
import time


# Checking for element is displayed(visible) before click and NOT displayed(NOT visible) after click on element
def test_visible_accordion(browser):
    accordion_page = AccordionPage(browser)

    accordion_page.visit()
    assert accordion_page.accordion_section_1_text.visible(), {accordion_page.accordion_section_1_text.is_displayed()}
    accordion_page.accordion_section_1_heading.click_elem()
    time.sleep(2)
    assert accordion_page.accordion_section_1_text.not_visible(), 'Element "p" is visible'

# Just empty line
