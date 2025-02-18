SHELL := /bin/bash

PROJECT_DIR := /home/ubuntu-42/tony-script
ENV_NAME := myenv

USER_INDEX ?= 1

run:
	@cd $(PROJECT_DIR) && \
	if [ ! -d "$(ENV_NAME)" ]; then \
		echo "Creando entorno virtual..."; \
		python3 -m venv $(ENV_NAME); \
	fi && \
	source $(ENV_NAME)/bin/activate && \
	pip install selenium pyautogui && \
	source .env && \
	export PADDEL_USER=$${PADDEL_USER$(USER_INDEX)} && \
	export PADDEL_PASS=$${PADDEL_PASS$(USER_INDEX)} && \
	echo "DEBUG: PADDEL_USER=$(PADDEL_USER)" && \
	echo "DEBUG: PADDEL_PASS=$(PADDEL_PASS)" && \
	xhost + && \
	xhost +si:localuser:$$USER && \
	python3 reserva_padel.py