from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome(
    executable_path="/home/imtoopunkforyou/prog/github/search-in-yandex/chromedriver")
url = "https://yandex.ru"


def close_browser():
    browser.close()
    browser.quit()

def test_pictures_on_yandexpage():
    """Тест, проверяющий ссылку на картинки на странице яндекса."""
    browser.get(url)
    pic_link = browser.find_element_by_css_selector("a[data-id=images]")
    assert pic_link, f'Ссылка на картики отсутсвует на {url}'
    
def test_pictures_link():
    """Тест, проверяющий фактический адрес ссылки Картинок."""
    browser.get(url)
    pic_link = browser.find_element_by_css_selector("a[data-id=images]")

    #Кликаем на ссылку Картинки
    pic_link.click()
    time.sleep(5)
    browser.switch_to_window(browser.window_handles[-1])

    #Проверяем ссылку после перехода
    assert "https://yandex.ru/images/" in browser.current_url, "Адрес ссылки Картинки отличается от https://yandex.ru/images/ или не является её производной"

def test_first_category():
    """Тест, открывающий первую категорию в картинках."""
    browser.get(url)
    pic_link = browser.find_element_by_css_selector("a[data-id=images]")
    pic_link.click()
    time.sleep(5)
    browser.switch_to_window(browser.window_handles[-1])

    #Находим и кликаем первую категорию в Картинках
    first_category = browser.find_element_by_css_selector("a.Link.PopularRequestList-Preview")
    first_category_text = first_category.text
    first_category.click()
    time.sleep(5)
    
    
    #Проверяем, верный ли текст в инпуте поиска(=в title страницы)
    assert first_category_text in browser.title, 'В строке поиска неверный текст' 

def test_first_picture(): 
    """Тест, открывающий первую картинку в первой категории."""
    browser.get(url)
    pic_link = browser.find_element_by_css_selector("a[data-id=images]")
    pic_link.click()
    time.sleep(5)
    browser.switch_to_window(browser.window_handles[-1])
    first_category = browser.find_element_by_css_selector("a.Link.PopularRequestList-Preview")
    first_category.click()
    time.sleep(5)

    #Находим первую картинку в категории и открываем её
    first_pic_in_category = browser.find_element_by_css_selector("a.serp-item__link")
    first_pic_in_category.click()
    time.sleep(5)
    
    #Проверяем, что открылась? записываем линк картинки
    original_size_pic = browser.find_element_by_css_selector("img.MMImage-Origin")
    original_size_pic_link = browser.current_url
    assert original_size_pic, 'Картинка не открылась в полном размере'


    """Проверяем работу кнопок в режиме просмотра картинок."""
    #Находим кнопки, нажимаем вперёд, нажимаем назад
    button_next = browser.find_element_by_css_selector("div.CircleButton_type_next")
    button_next.click()
    time.sleep(5)
    button_previous = browser.find_element_by_css_selector("div.CircleButton_type_prev")
    time.sleep(5)
    button_previous.click()
    time.sleep(5)

    #Проверяем, что картинка та же
    assert browser.current_url == original_size_pic_link, "Первая картинка была изменена"
    close_browser()