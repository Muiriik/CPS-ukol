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

venv:
	${PYTHON} -m venv ${VENV}

install: venv
	${VENV}/bin/pip install -r requirements.txt

run:
	FLASK_APP=./app.py \
	FLASK_ENV=development \
	flask run --port=8080

test:
	${VENV}/bin/pip install -e .
	${VENV}/bin/pytest


# EOF