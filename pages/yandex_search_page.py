import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class YandexSeacrhLocators():
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YANDEX_SEARCH_RESULT = (By.XPATH,
                                    "//a[@class='Link Link_theme_outer Path-Item "
                                    "link path__item link organic__greenurl']")


class YandexSearchPage(BasePage):
    @allure.step('Проверка наличия на странице поля поиска')
    def check_exist_search_field(self):
        return self.check_element_exists(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    @allure.step('Проверка появления таблицы с подсказками')
    def check_exist_search_suggest(self):
        return self.check_element_exists(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_SUGGEST)

    @allure.step('Проверка появления страницы результатов поиска')
    def check_exist_search_result(self):
        return self.check_element_exists(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_RESULT)

    @allure.step('Ввод поискового запроса')
    def enter_text_in_search_field(self, text):
        return self.find_element(YandexSeacrhLocators.
                                 LOCATOR_YANDEX_SEARCH_FIELD).send_keys(text)

    def push_keyboard_in_search_field(self, button):
        return self.find_element(YandexSeacrhLocators.
                                 LOCATOR_YANDEX_SEARCH_FIELD).send_keys(button)

    @allure.step('Проверка на совпадение с url первого результата поиска')
    def check_first_link(self, link):
        result_links = self.find_elements(YandexSeacrhLocators.
                                          LOCATOR_YANDEX_SEARCH_RESULT)
        if result_links:
            link_expected = result_links[0].get_attribute('href')
            return link_expected == link
        return False
