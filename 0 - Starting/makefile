FOLDER = ex03
FILE = tester.py

test : venv
	@mkdir -p $(FOLDER) && touch $(FOLDER)/$(FILE) && venv/bin/python $(FOLDER)/$(FILE) | cat -e

venv :
	python3.10 -m venv venv
	venv/bin/pip install -r requirements.txt

clean :
	rm -rf venv **/__pycache__
