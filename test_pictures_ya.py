from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome(
    executable_path="/home/imtoopunkforyou/prog/github/search-in-yandex/chromedriver")
url = "https://yandex.ru"

try:
    browser.get(url) #  1)зайти на yandex.ru
    pic_link = browser.find_element_by_css_selector("a[data-id=images]") # 2)Ссылка «Картинки» присутствует на странице
    print(pic_link.text)
    pic_link.click() # 3) кликаем на ссылку
    time.sleep(5)
    browser.switch_to_window(browser.window_handles[-1]) 
    print(browser.current_url) #проверить что перешлли на https://yandex.ru/images/ но открывается не тот урл
    first_category = browser.find_element_by_css_selector("a.Link.PopularRequestList-Preview")
    first_category.click() # 5) открыть первую категорию
    time.sleep(5)
    # if first_category.text in browser.current_url # тоже 5 пункт проверка что открылась и что вернуый текст
    first_pic_in_category = browser.find_element_by_css_selector("a.serp-item__link")
    first_pic_in_category.click()
    time.sleep(5)
    original_size_pic = browser.find_element_by_css_selector("img.MMImage-Origin")#6) Открыть 1 картинку , проверить что открылась
    original_size_pic_link = browser.current_url
    button_next = browser.find_element_by_css_selector("div.CircleButton_type_next")
    button_next.click()
    time.sleep(5)
    button_previous = browser.find_element_by_css_selector("div.CircleButton_type_prev")
    time.sleep(5)
    button_previous.click()
    #if browser.current_url == original_size_pic_link
    time.sleep(1000)

except Exception:
    print(Exception)
finally:
    browser.close()
    browser.quit()