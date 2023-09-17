SHELL := /bin/bash

# Please create .env file. Example file is provided as example.env
include .env

# Create virtual environment
venv:
	(\
	rm -rf penv; \
	virtualenv penv -p ${PY_PATH}; \
	source penv/bin/activate; \
	pip install -r requirements.txt; \
	)

# Activate the venv by executing . penv/bin/activate before
run_local:
	python -m autohubcompany

# build docker image
build_docker:
	docker build -t autohubcompany .

# Run docker container
run_docker: build_docker
	docker run -p 8080:8080 autohubcompany