install:
	pip install -r requirements.txt

check:
	python -m py_compile translate.py

run:
	python translate.py
