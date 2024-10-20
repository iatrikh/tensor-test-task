import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from poms.tensor.tensor_home_pom import TensorHome


class SbisContacts:

    def __init__(self, driver):
        self.driver = driver

    def find_and_click_tensor_banner(self):
        # По-другому не получалось обойти StaleElementReferenceException при переходе по ссылке на tensor.ru
        # WebDriverWait не помог.

        # return WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH, "//div[@id='contacts_clients']//a[@title='tensor.ru']")
        #     )
        # )

        while True:
            try:
                self.driver.find_element(
                    By.XPATH, "//div[@id='contacts_clients']//a[@title='tensor.ru']"
                ).click()
                break
            except StaleElementReferenceException:
                # chrome_driver.refresh()
                continue

        # Сайт tensor.ru открывается в соседней вкладке
        self.driver.switch_to.window(self.driver.window_handles[1])

        return TensorHome(self.driver)

    def find_current_region(self):

        while True:
            try:
                current_region = self.driver.find_element(
                    By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text')]"
                )
                current_region.text
                return current_region
            except StaleElementReferenceException:
                continue

    def find_parters_block(self):
        return self.driver.find_element(
            By.XPATH, "//div[@name='itemsContainer']//div[@id='city-id-2']"
        )

    def change_region_to(self, new_region):

        self.driver.find_element(
            By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text')]"
        ).click()

        time.sleep(0.5)  # Никак не получалось избежать этих двух слипов.

        self.driver.find_element(By.XPATH, f"//span[@title='{new_region}']").click()

        time.sleep(0.5)

        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text')]")
        #     )
        # ).click()

        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, f"//span[@title='{new_region}']"))
        # ).click()
