# Music App

This project is an example of how to use ManyToManyField in Django.

** This project is not ready for production **

## How to use it

1. Clone the repository

```bash
git clone
```

2. Create a virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the requirements

```bash
pip install -r requirements.txt
```

4. Create a .env file

```bash
touch .env
```

**.env**

```
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=dashfjkhskjdhaskdhksdkahdkjsgfiugehkhbfjkk
DJANGO_ACCOUNT_ALLOW_REGISTRATION=True
```

5. Run the migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the server

```
python manage.py runserver_plus
```
