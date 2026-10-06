from typing import Any

from selenium.webdriver.common.by import By


class UrbanRoutesPage:

    BASE_URL = "https://cnt-b877ebe7-2e16-494e-b636-e549591f0fab.containerhub.tripleten-services.com"

    FROM_LOCATOR = (By.ID, "from")
    TO_LOCATOR = (By.ID, "to")
    ERROR_LOCATOR = (
        By.XPATH,
        "//div[@class='error' and text()='Enter the address']"
    )
    TAXI_ICON = (By.CSS_SELECTOR, "button.button.round")

    MODO_ACTIVE_OPTIMAL = (By.CSS_SELECTOR, ".mode.active")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.BASE_URL)

    def enter_to(self, text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(text)

    def get_to_value(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")

    def enter_from(self, text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(text)

    def get_from_value(self) -> Any:
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_LOCATOR).text

    def get_taxi_icon(self):
        return self.driver.find_element(*self.TAXI_ICON).text

    def get_modo_active(self):
        return self.driver.find_element(*self.MODO_ACTIVE_OPTIMAL).text