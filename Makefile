#!/usr/bin/make -f
PYTHON = python
VENV = venv

help:
	@echo "Setup:"
	@echo "  venv           Setup virtual enviroment"
	@echo "  install        Install requirements"
	@echo ""
	@echo	"Application:"
	@echo	"  run            Run the application"
	@echo ""
	@echo "Testing:"
	@echo "  tests          Run tests"
	@echo ""

venv: venv/bin/python
venv/bin/python:
	${PYTHON} -m venv ${VENV}

install: venv
	${VENV}/bin/pip install -r requirements.txt

run: venv
	FLASK_APP=./src \
	FLASK_ENV=development \
	flask run --port=8080

test:
	${VENV}/bin/pytest


# EOF