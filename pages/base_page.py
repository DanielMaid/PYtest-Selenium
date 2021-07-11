from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """ Parent class for all pages.
    It contains all the generic methods and utilities for all pages."""

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def wait(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

    def do_click(self, by_locator):
        self.wait(by_locator).click()

    def do_send_keys(self, by_locator, text):
        self.wait(by_locator).send_keys(text)

    def get_element_text(self, by_locator):
        element = self.wait(by_locator)
        return element.text

    def is_visible(self, by_locator):
        element = self.wait(by_locator)
        return bool(element)

    def is_displayed(self, by_locator):
        return self.driver.find_element_by_css_selector(by_locator).is_visiable()

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_text(self, by_locator):
        element = self.wait(by_locator)
        return element.text

    def do_double_click(self, by_locator):
        ActionChains(self.driver).double_click(self.wait(by_locator)).perform()

    def scroll_into_view(self, by_locator):
        ActionChains(self.driver).move_to_element(self.wait(by_locator)).perform()

    def get_value(self, by_locator, attribute):
        element = self.wait(by_locator)
        return element.get_attribute(attribute)

    def clear(self, by_locator):
        element = self.wait(by_locator)
        element.clear()

