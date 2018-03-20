.PHONY: init pyuic pyrcc tests docs build pack clean

init:
	pip install -r requirements.txt

pyuic:
	python scripts/pyuic.py

pyrcc:
	python scripts/pyrcc.py

tests:
	python scripts/tests.py

docs:
	python scripts/docs.py

build:
	python setup.py sdist bdist_wheel

pack:
	pyinstaller -w {{ package }}/__main__.py -n {{ project }}

clean:
	python scripts/clean.py
