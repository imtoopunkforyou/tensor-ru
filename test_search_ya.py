from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(
    executable_path="/home/imtoopunkforyou/prog/github/tensor-ru/chromedriver")
url = "https://yandex.ru"

try:
    browser.get("https://yandex.ru")
    search_input = browser.find_element_by_id("text")
    search_input.clear()
    search_input.send_keys("Тензор")
    time.sleep(2)
    suggest_window = browser.find_elements_by_css_selector(
        "ul.mini-suggest__popup-content")  # подсказка
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)
    b_tags_set = browser.find_elements_by_tag_name("b")
    links = []
    for link in b_tags_set:
        link = link.text
        if link.count("."):
            links.append(link)
    print(links)
    time.sleep(10000000)
except Exception:
    print(Exception)
finally:
    browser.close()
    browser.quit()
