скачать проект
D:\>cd blog_git или D:\>git clone https://github.com/snssb/blog_git.git

создать виртуальное окружение
D:\blog_git>python -m venv venv

активировать (windows, linux - source venv/bin/activate)
D:\blog_git>.\venv\scripts\activate

установить необходимые пакеты
(venv) D:\blog_git>cd siteblog
(venv) D:\blog_git\siteblog>pip install -r requirements.txt

запустить сервер
(venv) D:\blog_git\siteblog>python manage.py runserver

Суперпользователь: Логин, Пароль - root, root

API:
"""Получить список постов  /api/v1/posts/"""

"""Обновить пост, за исключением фото  /api/v1/posts/1"""

"""Обновить фото поста  /api/v1/posts/photo/1/"""
