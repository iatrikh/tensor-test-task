import os
from selenium.webdriver.common.by import By
from poms.sbis.sbis_contacts_pom import SbisContacts
from selenium.webdriver.support.wait import WebDriverWait

from poms.sbis.sbis_download_pom import SbisDownload


class SbisHome:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def open_sbis_home(driver):

        sbis_url = "https://sbis.ru/"
        driver.get(sbis_url)

        return SbisHome(driver)

    def open_contacts_page(self):
        self.driver.find_element(By.XPATH, "//a[@href='/contacts']").click()
        return SbisContacts(self.driver)

    def open_local_versions(self):
        self.driver.find_element(
            "xpath", "//a[text()='Скачать локальные версии']"
        ).click()

        return SbisDownload(self.driver)
