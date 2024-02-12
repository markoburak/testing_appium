import time

from selenium.common import NoSuchElementException


class CompShared:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, selector: str, selector_type: str = "xpath") -> object:
        return self.driver.find_element(selector_type, selector)

    def get_element_text(self, selector: str, selector_type: str = "xpath") -> str:
        return self.driver.find_element(selector_type, selector).text

    def get_element_value(self, selector: str, selector_type: str = "xpath") -> str:
        return self.driver.find_element(selector_type, selector).get_attribute('value')

    def get_elements(self, selector: str, selector_type: str = "xpath") -> list:
        return self.driver.find_elements(selector_type, selector)

    def check_display_status_of_element(self, selector: str, selector_type: str = "xpath") -> bool:
        try:
            element = self.get_element(selector, selector_type)
            status = element.is_displayed()
        except NoSuchElementException:
            status = False
        return status

    def type_message(self, selector: str, message: str, selector_type: str = "xpath", timeout: int = 1) -> None:
        element = self.get_element(selector, selector_type)
        element.send_keys(message)
        time.sleep(timeout)
        return None

    def click_element(self, selector: str, selector_type: str = "xpath", timeout: int = 1) -> None:
        element = self.get_element(selector, selector_type)
        element.click()
        time.sleep(timeout)
        return None
