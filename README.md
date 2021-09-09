# menuapp
## Requirements
### All needed packages are in requirements.txt
```pip install requirements.txt ```
# SMTP
### All needed credentials are in setting.py (no needed setup)
# Basic setup
### Linux
```brew install rabbitmq```
### Windows
<https://www.rabbitmq.com/install-windows.html#installer>
### Make a postgres server and paste credentials into menuapp/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'XXXX',
        'USER': 'XXXX',
        'PASSWORD': 'XXXX',
        'HOST': 'XXXX',
        'PORT': 'XXXX',
    }
}
```
``` python manage.py makemigrations``` \
```python manage.py migrate ``` \
Create super user (App doesn't have a register functions) \
```python manage.py createsuperuser```

## Running a server
```python manage.py runserver```

## Running a tests
```manage.py test```

## Starting a Celery tasks (sending emails)
### Windows
```celery -A menuapp worker --pool=solo -l info```

```celery -A menuapp beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler```
### Linux (not sure about commands, didn't tested them)
```celery -A menuapp worker -l info```

```celery -A menuapp beat -l info```
## Urls
<http://127.0.0.1:8000/>  Main view for API by browser \
<http://127.0.0.1:8000/docs/> Docs for API 

## Linter
I'm using flake8 with-max-line-length = 120 (for Django purposes)



