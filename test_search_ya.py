from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(
    executable_path="/home/imtoopunkforyou/prog/github/tensor-ru/chromedriver")
url = "https://yandex.ru"
keywrd = "Тензор"

def close_browser():
    browser.close()
    browser.quit()

def test_search_input():
    """Тест, проверяющий наличие поля поиска"""
    browser.get(url)
    time.sleep(5)
    search_input = browser.find_element_by_id("text")
    assert search_input, f'На странице {url} нет поля для поиска'


def test_suggest_window():
    """Тест, проверяющий есть ли таблица подсказок"""
    browser.get(url)
    search_input = browser.find_element_by_id("text")
    search_input.clear()
    search_input.send_keys(keywrd)
    time.sleep(5)
    suggest_window = browser.find_elements_by_css_selector("ul.mini-suggest__popup-content")
    assert suggest_window, 'Таблица с подсказками не появилась'

def test_search_result():
    """"Тест, проверяющий, есть ли в первых 5 результатах поиска tensor.ru"""
    links = []
    browser.get(url)
    search_input = browser.find_element_by_id("text")
    search_input.clear()
    search_input.send_keys(keywrd)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)
    b_tags_set = browser.find_elements_by_tag_name("b")
    for link in b_tags_set:
        link = link.text
        if link.count("."):
            links.append(link)
    assert links.index("tensor.ru") <= 4, 'В первых 5 результатах поиска отсутствует tensor.ru'
    close_browser()

