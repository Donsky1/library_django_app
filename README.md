# library_django_app
📚 Project: Library Management API: Django APP

Stack + Libraries: Django, PostgreSQL, Docker Compose, DRF, JWT, DRF Spectacular, Psycopg2
Linters: Ruff, Mypy

Steps (DEV): SQLite3:
1. Install UV
2. cd library_django_app
3. make install
4. source .venv/bin/activate
5. make superuser
6. make run

OR

Steps (DEV): PostgreSQL:
1. Install UV
2. uv sync
3. source .venv/bin/activate
4. Change example.env to IS_SQLITE3=False
5. docker compose up -d
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver or uv run manage.py runserver