# Тестовое задание. Тензор.
---

## Описание
Реализованы два теста:
1) проверка на соответствие первой строки поиска URL tensor.ru;
2) проверка идентичности картинок в процессе пагинации.

---

## Как установить проект
1) Создайте копию проекта командой `git clone https://github.com/arthur-akhmadullin/tensor.git`. Копия будет помещена в папку "tensor".
2) Перейдите в папку "tensor", выполнив в командной строке: `cd tensor`. 
3) Создайте виртуальное окружение, выполнив команду `python -m venv <название-вашего-виртуального-окружения>`.
4) Активируйте виртуальное окружение, выполнив команду `<название-вашего-виртуального-окружения>\Scripts\activate` (Windows) или `. <название-вашего-виртуального-окружения>/bin/activate` (Linux).
5) Установите библиотеки, последовательно выполнив команды: `python -m pip install`, `pip install -r requirements.txt`.

---

## Запуск тестов
Для работы с тестами необходимо установить драйвер браузера `chromedriver.exe`, который можно скачать по ссылке https://chromedriver.chromium.org/downloads. Файл поместить в корневую папку `tensor`. В файле `conftest.py` прописать расположение файла в параметре `executable_path`, например **executable_path=r"C:\chromedriver.exe"**.
Запуск тестов производится командой `pytest <путь к файлу, содержащему тесты>`:

1) `pytest tests/test_yandex_search.py` - тест поисковой строки
2) `pytest tests/test_yandex_pictures.py` - тест Яндекс-картинок

---

## Получение отчетов
Для формирования отчетов используется библиотека `allure-pytest`.
Чтобы создать отчет, запустите тест с параметром `--alluredir=<путь к директории с отчетами>`.
Например, **pytest --alluredir=reports/ tests/test_yandex_search.py**. По завершению тестов в папку reports будут помщены отчеты в формате json.
