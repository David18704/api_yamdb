### Описание проекта:
Учебный проект, предназначенный для отработки навыков и применение теории при командной
разработки API для веб приложения YaMDb, базируемых на фреймворке Django и модуле Django Rest Framework.
Для обеспечения контороля прав доступа в проекте используется модуль JWT-токен.

### Установка и запуск проекта:

Клонировать репозиторий и перейти в него в командной строке (испольщуем ssh):

```
git clone https://github.com/David18704/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env (для Windows) или python -m venv venv (для Windows на Mac или Linux)
```

```
source venv/Scripts/activate (для Windows) или source venv/bin/activate (для macOS или Linux)
```

Обновить pip до последней версии:
```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Дополнительно установить модули Simple JWT и django_filters:

```
pip install django-filter
pip install djangorestframework_simplejwt 
```

Выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры использования API:

```
Детальное описание и примеры работы API проекта представлены в 
документации: http://127.0.0.1:8000/redoc/ в формате ReDoc.
