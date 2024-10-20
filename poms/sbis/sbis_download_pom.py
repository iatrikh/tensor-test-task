import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SbisDownload:

    def __init__(self, driver):
        self.driver = driver

    def find_and_download_win_plugin(self):
        self.driver.find_element(
            By.XPATH, "//a[text()='Скачать локальные версии']"
        ).click()

        self.driver.find_element(
            By.XPATH, "//a[contains(text(), 'Скачать (Exe')]"
        ).click()

        WebDriverWait(self, 15).until(
            lambda _: os.path.exists("downloads\\sbisplugin-setup-web.exe")
        )
