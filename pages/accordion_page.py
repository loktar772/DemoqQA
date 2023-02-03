from pages.base_page import BasePage
from components.components import WebElement


# Creating class AccordionPage(for page 'https://demoqa.com/accordian')
class AccordionPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.accordion_section_1_heading = WebElement(driver, '#section1Heading')
        self.accordion_section_1_text = WebElement(driver, '#section1Content > p')
        self.not_elem = WebElement(driver, 'p>p')


