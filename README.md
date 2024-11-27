# Лабораторная работа 1

## Как выполнять

Выполнять согласно алгоритму в [up09-index](https://github.com/31isr/up09-index)

## 1. Создание Django проекта

### 1. Создание папки под проект

Запустите `git bash`

`mkdir "название_папки"`
`mkdir` - создает папку

`cd "название_папки"`
`cd` - перемещает shell в папку

### 2. Создание виртуальной среды

`python -m venv .venv`

-   `-m название_модуля` - найти модуль в sys.path и запустить его py файл как скрипт
-   `.venv` - название папки, в которой будут храниться файлы для виртуальной среды

### 3. Активация виртуальной среды

#### Unix системы

`source .venv/activate`

### 4. Установка Django

`python -m pip install Django`

### 5. Инициализация приложения

`mkdir lab1` - создаем папку под проект

`django-admin startproject lab1 lab1` - инициализируем проект

-   `lab1` (первое) - название проекта
-   `lab1` - название папки

> [!warning]
> Название проекта не должно совпадать с названием Python модулей (напирмер Django, test, random и так далее)

### 6. Запуск сервера разработчика

`cd lab1` - переход в папку, которую создали [[#5. Инициализация приложения|при инициализации проекта]]
`py manage.py runserver`

-   `py` - название бинарного файла Python интерпритора, который вы установили (может отличаться, например `python`, `python3`, `python3.12`...)
-   `manage.py` - название файла
-   `runserver` - название команды, указанной в `manage.py`

Сервер развернется на первом свободном порту, начиная с 8000. Успешный вывод команды должен выглядеть следующим образом

```sh
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 25, 2024 - 04:44:23
Django version 5.1.3, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

### Источники

1. [Документация Django](https://docs.djangoproject.com/en/5.1/intro/install/)

---

## 2. Разработка маршрута "about"

### 1. Создание маршрута "about"

1. Создайте файл `lab1/views.py`

```python
from django.shortcuts import render
# Импорт функции `render` из модуля `django.shortcuts`.
# Эта функция используется для отображения HTML-шаблонов
# с передачей в них данных.

def about(req):
    # Определение функции `about`, которая принимает один параметр `req`.
    # Обычно `req` — это объект запроса (request), передаваемый Django при вызове функции.

    return render(req, "about.html")
    # Функция `render` генерирует HTTP-ответ с указанным HTML-шаблоном.
    # Здесь `req` — объект запроса, передаваемый для обработки, а `"about.html"` —
    # имя файла HTML-шаблона, который будет отображён пользователю.
    # Если требуется передать данные в шаблон, их можно указать третьим параметром
    # в виде словаря (например, `{"key": "value"}`).
```

2. Добавьте новую схему в переменную `urlpatterns` в файле `lab1/urls.py`

```python
urlpatterns = [
    # Объявление переменной `urlpatterns`, которая содержит список маршрутов
    # (URL-адресов) для сопоставления запросов с обработчиками.

    path('admin/', admin.site.urls),
    # Маршрут, связывающий URL `/admin/` с встроенным интерфейсом администратора Django.
    # `admin.site.urls` — это готовый обработчик, предоставляемый Django для работы с админкой.

    path('about/', views.about),
    # Маршрут, связывающий URL `/about/` с функцией `about` из модуля `views`.
    # Когда пользователь открывает `/about/`, вызывается функция `about`, которая,
    # в данном случае, возвращает HTML-шаблон "about.html".
]
```

3. Создайте папку `lab1/templates`
4. В папке создайте `about.html`, который должен пока отображать заголовок первого уровня "Страница обо мне"
5. В файле `lab1/urls.py` импортируйте views

```python
from django.contrib import admin
from django.urls import path, include
from . import views

...
```

6. В файле `lab1/settings.py` добавьте папку с шаблонами в массив `DIRS`

```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # лист с названиями папок, в которых будут храниться шаблоны
        'APP_DIRS': True,
...
```

### 2. Работа со статичными файлами

1. Создайте папки `lab1/static/css`
2. В папке `lab1/static/css` создайте файл `style.css` с содержанием

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

3. Добавьте стилей в файл
    - `body` должен быть во всю высоту
    - весь контент должен быть по центру экрана
    - размер текста должен быть `3rem`
    - задник должен быть темным
    - текст должен быть светлым
    - тэги `h1` и `p` должны выравниваться по центру
4. Добавьте импорт в файл `lab1/settings.py` для того, чтобы Django мог обрабатывать путь до файлов

```python
...
import os # эта строчка
from pathlib import Path
...
```

5. В конце этого же файла создайте переменную `STATICFILES_DIRS`, которая содержит лист с одним элементом - `os.path.join(BASE_DIR, 'static')`
6. Подключите статические файлы в шаблоне `about.html`

```html
<!doctype html>
{% load static %} - эта строчка
<html lang="en"></html>
```

7. Добавьте стили на страницу

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="stylesheet" href="{% static 'css/style.css' %}" />
- эта строчка
<title>Обо мне</title>
```

8. Запустите сервер и проверьте работает ли маршрут `about` по этой ссылке `localhost:8000/about`

> [!info] Задание 1
> Попробуйте добавить JavaScript файл, который будет выводить в консоли надпись `Добро пожаловать на мой сайт`

> [!info] Задание 2
> Создайте главную страницу, которая будет открываться по маршруту `/` и отображать шаблон с заголовком первого уровня "Главная страница". Подключите JS и CSS файлы

## 3. Создание приложения "posts"

### 1. Инициализация приложения

1. `py manage.py startapp posts` - создает папку под приложение posts

### 2. Создание пути "posts"

1. В файле `posts/urls.py` добавьте путь, который описывает маршрут `/`

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list),
]
```

2. Добавьте `posts` как приложение в файл `lab1/settings.py`

```python
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts' # <-------------
]
...
```

3. Создайте папку с шаблонами внутри приложения posts, внутри этой папки создайте папку с названием posts, а внутри этой папки создайте файл `posts_list.html` с заголовком первого уровня `Посты`
4. Создайте файл `posts/urls.py`, который будет описывать маршруты внутри маршрута `localhost:8000/posts/*`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list),
]
```

5. В файле `posts/views.py` добавьте новую функцию, которая будет отвечать на запрос `localhost:8000/posts` страницей `posts_list.html`

```python
from django.shortcuts import render

def posts_list(req):
    return render(req, 'posts/posts_list.html')
```

6. Добавьте маршрут `localhost:8000/posts` в проект. Добавьте в лист `urlpatterns` в `lab1/urls.py` новый маршрут с помощью функции `include`

```python
from django.urls import path, include # <-- импорт функции include
...
    path('posts/', include('posts.urls')),
...
```

7. Проверьте работает ли приложение `posts` перейдя по [этой ссылке](localhost:8000/posts)

> [!info] Задание 3
> Попробуйте добавить приложение communities, которое будет располагаться по маршруту "communities"
