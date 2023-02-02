# from pages.demoqa import DemoQa
from selenium.common.exceptions import ElementNotVisibleException
from pages.elements_page import ElementsPage
from pages.accordion_page import AccordionPage
import time


# from components.components import WebElement

# Checking for text element is displayed(visible)
def test_visible_btn_sidebar(browser):
    vis_el = ElementsPage(browser)

    vis_el.visit()
    vis_el.side_bar_button_first.click_elem()
    time.sleep(3)
    # assert vis_el.side_bar_first_textbox.exist()
    try:
        assert vis_el.side_bar_first_textbox.visible()
    except ElementNotVisibleException:
        return False
    return True


# Checking for element is NOT displayed(NOT visible)
def test_not_visible_btn_sidebar(browser):
    not_vis_el = ElementsPage(browser)
    not_vis_el.visit()
    assert not_vis_el.side_bar_first_checkbox.visible()
    not_vis_el.side_bar_button_first.click_elem()
    time.sleep(2)
    assert not_vis_el.side_bar_first_checkbox.not_visible()


def test_visible_default_accordion(browser):
    accordion_vis = AccordionPage(browser)

    accordion_vis.visit()
    assert accordion_vis.accordion_section_1_text.visible()
    accordion_vis.accordion_section_1_heading.click_elem()
    # set window size
    browser.set_window_size(width=1000, height=300)
    time.sleep(2)
    assert accordion_vis.accordion_section_1_text.not_visible()
    # set window size
    browser.set_window_size(width=1000, height=1000)
    accordion_vis.refresh()
    assert accordion_vis.accordion_section_1_text.visible()
# Just empty line
