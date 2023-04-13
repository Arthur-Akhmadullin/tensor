import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class YandexPicturesLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SERVICES_BUTTON = (By.CLASS_NAME, "services-suggest__icons-more")
    LOCATOR_YANDEX_PICTURES_BUTTON = (By.XPATH, "//a[@aria-label='Картинки']")
    LOCATOR_YANDEX_PICTURES_CATEGORIES = (By.CSS_SELECTOR, '[data-grid-name="im"]')
    LOCATOR_YANDEX_PICTURES_SEARCH_FIELD = (By.CSS_SELECTOR, 'input[name="text"]')
    LOCATOR_YANDEX_PREVIEW_PICTURES = (By.CLASS_NAME, 'serp-item')
    LOCATOR_YANDEX_OPENED_PICTURE = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_YANDEX_NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next')
    LOCATOR_YANDEX_PREV_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev')


class YandexPicturesPage(BasePage):
    @allure.step('Проверка наличия на странице поля поиска')
    def check_exists_search_field(self):
        return self.check_element_exists(YandexPicturesLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    @allure.step('Проверка наличия на странице кнопки "Все сервисы" ')
    def check_exists_services_button(self):
        return self.check_element_exists(YandexPicturesLocators.LOCATOR_YANDEX_SERVICES_BUTTON)

    @allure.step('Проверка наличия на странице кнопки "Картинки" ')
    def check_exists_pictures_button(self):
        return self.check_element_exists(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_BUTTON)

    @allure.step('Установка курсора в поле поиска')
    def get_up_search_field(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_SEARCH_FIELD).click()

    @allure.step('Открытие меню "Все сервисы" ')
    def click_services_button(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_SERVICES_BUTTON).click()

    @allure.step('Открытие сервиса "Картинки" ')
    def click_pictures_button(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_BUTTON).click()

    @allure.step('Получение первой категории картинок')
    def get_pictures_first_category(self):
        elements = self.find_elements(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_CATEGORIES)
        return elements[0]

    @allure.step('Открытие первой категории картинок')
    def click_pictures_first_category(self):
        self.get_pictures_first_category().click()

    @allure.step('Получение поля поиска на странице картинок')
    def get_pictures_search_field(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_SEARCH_FIELD)

    @allure.step('Переход на первую картинку')
    def click_first_preview_picture(self):
        return self.find_elements(YandexPicturesLocators.LOCATOR_YANDEX_PREVIEW_PICTURES)[0].click()

    @allure.step('Получение открытой картинки')
    def get_opened_picture(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_OPENED_PICTURE)

    @allure.step('Нажатие на кнопку "Следующая картиника" ')
    def click_next_button(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_NEXT_BUTTON).click()

    @allure.step('Нажатие на кнопку "Предыдущая картиника" ')
    def click_prev_button(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PREV_BUTTON).click()

    @allure.step('Проверка совпадения ссылки и URL "Яндекс-картинки" ')
    def check_pictures_link(self, link):
        link_pictures = self.get_current_url()
        if link_pictures:
            return link in link_pictures
        return False
