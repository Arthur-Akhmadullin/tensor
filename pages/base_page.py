from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.ya.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time). \
            until(ec.presence_of_element_located(locator),
                  message=f"Не найден элемент локатора {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time). \
            until(ec.presence_of_all_elements_located(locator),
                  message=f"Не найдены элементы локатора {locator}")

    def open_site(self):
        return self.driver.get(self.base_url)

    def check_element_exists(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def get_current_url(self):
        return self.driver.current_url

    def go_to_second_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
