clean_pycache:
	find . -type d -name __pycache__ -exec rm -r {} \+

run:
	python3 main.py

create-venv:
	python3 -m venv venv

install-requirements:
	venv/bin/python3 -m pip install --upgrade pip
	venv/bin/pip install -r requirements.txt