sync:
	uv sync

# install project with sqlite3
install:
	cat example.env > .env
	make sync
	uv run backend/manage.py migrate


# create superuser
superuser:
	uv run backend/manage.py createsuperuser


# run development server
run:
	uv run backend/manage.py runserver


ruff-cf:
	clear && ruff check . --fix && ruff format .

ruff-c:
	clear && ruff check . && ruff format --check .
