from pages.base_page import BasePage
from components.components import WebElement


# Creating class ElementsPage(for page 'https://demoqa.com/elements')
class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        self.icon = WebElement(driver, '#app > header > a > img')
        self.text_please = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.text_center = WebElement(driver, '.main-header')
        self.side_bar_button_first = WebElement(driver, 'span.group-header')
        self.side_bar_first_textbox = WebElement(driver, '.menu-list > li#item-0')
        self.side_bar_first_checkbox = WebElement(driver, '.menu-list > li#item-1')
        self.btns_first_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')

        super().__init__(driver, self.base_url)

# Just empty line
