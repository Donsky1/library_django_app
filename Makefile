sync:
	uv sync

install:
	cat example.env > .env
	make sync


ruff-cf:
	clear && ruff check . --fix && ruff format .

ruff-c:
	clear && ruff check . && ruff format --check .
