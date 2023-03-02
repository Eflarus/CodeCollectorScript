# Code collector
Используется для удобного добавления кода в отчеты по курсовым и прочим работам.

Скрипт для сборки кода всего проекта в один файл. Сборка происходит по всем файлам из текущей и дочерних директорий.


### Можно настроить:
- файл вывода
- маски для исключения файлов или директорий из выдачи _(подобно gitignore)_
- паттерн разделителя между файлами

### Пример
Cкрипт с дефолтными настройками генерирует подобный файл:
```
__________________________________________________
main.py
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
from app import app


if __name__ == '__main__':
    app.run()
    print('bye')
__________________________________________________
config.py
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
import os
from dotenv import load_dotenv


class Config(object):
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    DEBUG = False
    TESTING = False
__________________________________________________
requirements.txt
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
click==8.1.3
cx-Oracle==8.3.0
dnspython==2.2.1
__________________________________________________
app/__init__.py
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
import datetime
import os
...
```