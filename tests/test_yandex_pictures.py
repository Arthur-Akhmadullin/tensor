import time
import allure

from pages.yandex_pictures_page import YandexPicturesPage


@allure.feature('Тест сервиса Яндекс-картинки')
@allure.story('Тест проверяет идентичность картинок в процессе пагинации ')
def test_pictures(browser):
    yandex = YandexPicturesPage(browser)
    yandex.open_site()

    assert yandex.check_exists_search_field()
    yandex.get_up_search_field()
    assert yandex.check_exists_services_button()
    yandex.click_services_button()
    time.sleep(2)
    assert yandex.check_exists_pictures_button()
    yandex.click_pictures_button()
    yandex.go_to_second_tab()
    time.sleep(2)

    assert yandex.check_pictures_link('https://yandex.ru/images'), \
        "Ссылка не совпадает с текущим URL"

    text_category = yandex.get_pictures_first_category().get_attribute('data-grid-text')
    yandex.click_pictures_first_category()
    text_search_field = yandex.get_pictures_search_field().get_attribute('value')
    assert text_category == text_search_field, f"{text_category} не совпадает с {text_search_field}"

    yandex.click_first_preview_picture()
    src_first_picture = yandex.get_opened_picture().get_attribute('src')
    assert src_first_picture, 'Картинка не найдена'

    yandex.click_next_button()
    src_second_picture = yandex.get_opened_picture().get_attribute('src')
    assert src_first_picture != src_second_picture, "Картинка не сменилась"

    yandex.click_prev_button()
    src_again_first_picture = yandex.get_opened_picture().get_attribute('src')
    assert src_again_first_picture == src_first_picture
    time.sleep(1)
