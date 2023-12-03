# Запуск django приложения

1. Создать виртуальное окружение

```python
python3 -m venv venv
```

2. Активировать виртуальное окружение

- linux

```
source ./venv/bin/activate
```

- windows

```
./venv/bin/Activate.ps1
```

3. Установить зависимости проекта

```
pip install -r requirements.txt
```

4. Сделать миграции

```
python manage.py makemigrations

python manage.py migrate
```

5. Запустить сервер

```
python manage.py runserver
```
