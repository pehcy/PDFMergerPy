### MAIN TARGET ###
.PHONY = virtual install build-requirements pfpdf2
all: check test

python = python3
PYTHON := $(BIN)/$(python)
project_name = pdf_merger

virtual: venv/bin/pip

.venv.bin/pip:
	virtualenv -p /usr/bin/${PYTHON} .venv

# install PyPDF2 library
.venv/bin/pypdf2:
	.venv/bin/pip install -U PyPDF2

run:
	${PYTHON} ${project_name}.py

clean:
	rm -f MANIFEST
	rm -rf build dist
