import allure
from selenium.webdriver import Keys

from pages.yandex_search_page import YandexSearchPage


@allure.feature('Тест результатов поиска')
@allure.story('Тест проверяет, что первая ссылка ведет на сайт tensor.ru')
def test_search(browser):
    yandex = YandexSearchPage(browser)
    yandex.open_site()
    assert yandex.check_exist_search_field(), "Не найден локатор поле поиска"
    yandex.enter_text_in_search_field("Тензор")
    assert yandex.check_exist_search_suggest(), "Не найден локатор таблица с подсказками"
    yandex.push_keyboard_in_search_field(Keys.ENTER)
    assert yandex.check_exist_search_result(), "Не найдена страница с результатами поиска "
    assert yandex.check_first_link('https://tensor.ru/'), "Ссылки не совпадают"
