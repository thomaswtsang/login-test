.PHONY: deps lint test

deps:
	pip install -r requirements-dev.txt -r requirements-test.txt

lint:
	flake8 tests/

test:
	pytest tests/
