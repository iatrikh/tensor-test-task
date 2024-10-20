from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

from poms.tensor.tensor_about_pom import TensorAbout


class TensorHome:

    def __init__(self, driver):
        self.driver = driver

    def find_people_block(self):
        while True:
            try:
                people_block = self.driver.find_element(
                    By.XPATH, "//p[text()='Сила в людях']"
                )
                return people_block
            except StaleElementReferenceException:
                continue

    def find_and_open_about(self):

        self.driver.find_element(
            By.XPATH, "//a[@href='/about' and text()='Подробнее']"
        ).click()

        return TensorAbout(self.driver)
