# Assignment

This project runs a django web server that responds to a single request:

`GET /smallest/[start]/[stop]/`

Where start and stop are 2 integers

It then returns that smallest positive integer that is divisible by all integers
starting at `[start]` and stopping at `[stop]`.

For example
`GET /smallest/3/5/` will return `60` since its the smalles number divisible by
`3`, `4` and `5`

# Installing

Clone the project with:

`git clone https://github.com/rwblokzijl/west-assignment.git`

All subsequent commands will be run from the project root directory:

`cd west-assignment`

In a development environment the project needs some dependencies installed.
Install them with pipenv:

`pipenv install`

# Running the project

## Production
In production the project can be deployed with docker-compose

If you have changed dependencies through pipenv, update the `requirements.txt`
before deploying with:

`pipenv lock --requirements > requirements.txt`

Now deploy with docker-compose:

`docker-compose up --build`

The API can now be reached at the default web port with
http://localhost/smallest/1/25/

## Development

The project can be run for development with:

`pipenv run python src/manage.py runserver`

This enables hot reload, debug and other django development features.

The API can now be reached at port 8000 with
http://localhost:8000/smallest/1/25/

# Running tests

Running most tests can be done with:

`pipenv run python -m unittest`

Slow running tests can be run by setting the environment variable `$SLOW` with:

`SLOW=1 pipenv run python -m unittest` (These take about 30 seconds on my
laptop.)

# Relevant files

Most of the interesting engineering is limited to the following files:

- src/assignment/views.py
- test/assignment/test_views.py
- Dockerfile
- docker-compose.yml

# Other notes

- Pipenv can be skipped by installing from `requirements.txt`
- A Makefile is available with easy shortcuts to all the commands mentioned in
  this file.
- A .projections file is available that maps src files to test files.

