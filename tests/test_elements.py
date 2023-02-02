from pages.elements_page import ElementsPage


def test_elements(browser):
    t_elements = ElementsPage(browser)

    t_elements.visit()
    assert t_elements.btns_first_menu.check_count_elements(9)
