all: lock

.PHONY: test

install:
	pipenv install

lock:
	pipenv lock --requirements > requirements.txt

build: lock
	docker-compose build

run: lock
	docker-compose up --build

test:
	pipenv run python -m unittest

test_all:
	SLOW=1 pipenv run python -m unittest

dev:
	pipenv run python src/manage.py runserver
