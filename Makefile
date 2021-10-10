

environment:
	pwd
	ls
	if [ -e ./env ]; then rm -fr ./env; fi
	if [ -e ./poetry.lock ]; then rm ./poetry.lock; fi
	python3 -m venv env
	. env/bin/activate
	pip install poetry
	pip install mido
	pip install rtmidi
	pip install pytest
	poetry install

