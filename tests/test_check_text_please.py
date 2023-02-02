from pages.elements_page import ElementsPage


# Checking for text on the page is equal to given and existence of the elements
def test_page_elements(browser):
    text_eq = ElementsPage(browser)
    text_eq.visit()

    # Checking for text on the page is equal to given
    assert text_eq.text_please.get_text() == 'Please select an item from left to start practice.'
    assert text_eq.text_center.get_text() == 'Elements'

    # Checking if element exists
    assert text_eq.icon.exist()
    assert text_eq.side_bar_button_first.exist()
    assert text_eq.side_bar_first_textbox.exist()

# Just empty line
