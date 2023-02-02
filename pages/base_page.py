# Creating Base page class (for page https://demoqa.com/)
class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    # Creating Base methods
    # Creating method for open page
    def visit(self):
        return self.driver.get(self.base_url)

    # Creating method to go page back
    def back(self):
        self.driver.back()

    # Creating method to go page forward
    def forward(self):
        self.driver.forward()

    # Creating method to refresh page
    def refresh(self):
        self.driver.refresh()

    # Creating method to get current page url
    def get_url(self):
        return self.driver.current_url

    # Creating method to get current page title
    def get_title(self):
        return self.driver.title

    # Creating method to get current page title
    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

# Just empty line
