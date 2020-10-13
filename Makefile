PYTHON = python3
project_name = pdf_merger

virtual: venv/bin/pip

.venv.bin/pip:
			virtualenv -p /usr/bin/${PYTHON} .venv

run:
			${PYTHON} ${project_name}.py
