# Define variables
PIP := pip3
PYTHON := python3
SELENIUM_DIR := selenium-python-demo
CYPRESS_DIR := cypress-demo
CYPRESS_LOCAL_RUN := npx cypress run
CYPRESS_CLOUD_RUN := lambdatest-cypress
PROJECT_NAME := Handling canvas elements with Cypress & Selenium Python

.PHONY: install
install:
	cd $(SELENIUM_DIR)
	$(PIP) install -r selenium-python-demo/requirements.txt
	@echo "Set env vars LT_USERNAME & LT_ACCESS_KEY"
    # Procure Username and AccessKey from https://accounts.lambdatest.com/security
	export LT_USERNAME= $(LT_USERNAME)
	export LT_ACCESS_KEY= $(LT_ACCESS_KEY)

.PHONY: test
test:
    export NODE_ENV = test

.PHONY: test
local-canvas-automation-python:
	@echo "SELENIUM_DIR: $(SELENIUM_DIR)"
	- cd $(SELENIUM_DIR) && $(PYTHON) canvas_autogui.py

cloud-canvas-automation-python:
	@echo "SELENIUM_DIR: $(SELENIUM_DIR)"
	- cd $(SELENIUM_DIR) && $(PYTHON) canvas_bar_graph.py

local-canvas-automation-cypress:
	@echo "CYPRESS_DIR: $(CYPRESS_DIR)"
	@echo "CYPRESS_LOCAL_RUN: $(CYPRESS_LOCAL_RUN)"
	- cd $(CYPRESS_DIR) && $(CYPRESS_LOCAL_RUN) --browser chrome --headed

cloud-canvas-automation-cypress:
	@echo "CYPRESS_DIR: $(CYPRESS_DIR)"
	@echo "CYPRESS_CLOUD_RUN: $(CYPRESS_CLOUD_RUN)"
	- cd $(CYPRESS_DIR) && $(CYPRESS_CLOUD_RUN) run

.PHONY: clean
clean:
    # This helped: https://gist.github.com/hbsdev/a17deea814bc10197285
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
	@echo "Clean Succeded"

.PHONY: distclean
distclean: clean
	rm -rf venv

.PHONY: help
help:
	@echo ""
	@echo "install : Install project dependencies"
	@echo "clean : Clean up temp files"
	@echo "local-canvas-automation-python : Canvas handling with Selenium Python on local grid"
	@echo "cloud-canvas-automation-python : Canvas handling with Selenium Python on cloud grid"
	@echo "local-canvas-automation-cypress : Canvas handling with Cypress on local machine"
	@echo "cloud-canvas-automation-cypress : Canvas handling with Cypress on LambdaTest cloud grid"