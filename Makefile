

environment:
	rm -fr ./env
	python -m venv env
	. env/bin/activate
	poetry install

