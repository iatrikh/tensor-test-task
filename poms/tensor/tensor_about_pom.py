from selenium.webdriver.common.by import By


class TensorAbout:

    def __init__(self, driver):
        self.driver = driver

    def find_images_in_rabotayem_block(self):
        return self.driver.find_elements(
            By.XPATH,
            "//div[@class='s-Grid-container']//div[contains(@class, '-image')]//img",
        )
