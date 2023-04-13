import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, executable_path=r"E:\Python2023\QA\Tensor\chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()
