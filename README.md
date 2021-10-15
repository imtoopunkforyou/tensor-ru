# tensor-ru
Test task for tensor.ru as a tester

# Задача
Необходимо автоматизировать проверку двух сценариев:
1. Поиск в яндексе
2. Картинки в яндексе

# Сценарий "Поиск в яндексе"
* Зайти на yandex.ru
* Проверить наличия поля поиска
* Ввести в поиск Тензор
* Проверить, что появилась таблица с подсказками (suggest) 
* При нажатии Enter появляется таблица результатов поиска
* В первых 5 результатах есть ссылка на tensor.ru

# Сценарий "Картинки в яндексе"
* Зайти на yandex.ru
* Ссылка «Картинки» присутствует на странице
* Кликаем на ссылку
* Проверить, что перешли на url https://yandex.ru/images/
* Открыть 1 категорию, проверить что открылась, в поиске верный текст
* Открыть 1 картинку , проверить что открылась
* При нажатии кнопки вперед  картинка изменяется
* При нажатии кнопки назад картинка изменяется на изображение из шага 6. Необходимо проверить, что это то же изображение.

# Стэк
* Python 3
* Selenium Webdriver
* Pytest



# Установка и запуск
Вы можете использовать виртуальное окружение на вашей машине, если вам так удобнее.
Для запуска потребуется скачать драйвер для вашей версии GoogleChrome. Все драйвера доступны по [ссылке](https://chromedriver.chromium.org/downloads).
В аргументе ``executable_path`` необходимо указать абсолютный путь до скаченного драйвера.

* ``git clone https://github.com/imtoopunkforyou/tensor-ru.git``
* ``cd ~/tensor-ru``
* ``pip install -U pip``
* ``pip install -r requirements.txt``
* ``pytest -v test_search_ya.py`` для запуска сценария "Поиск в Яндексе"
* ``pytest -v test_pictures_ya.py`` для запуска сценария "Картики в яндексе"
