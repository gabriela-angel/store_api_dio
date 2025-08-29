# -----    RULES     -----
run:
	@echo "Starting the FastAPI server..."
	@uvicorn store.main:app --reload

precommit-install:
	@echo "Installing pre-commit hooks..."
	@pipenv run pre-commit install

test:
	@echo "Running tests with pytest..."
	-@PYTHONPATH=$PYTHONPATH:$(pwd) pipenv run pytest -v tests/ || true

test-matching:
	@echo "Running tests with pytest for matching files..."
	-@PYTHONPATH=$PYTHONPATH:$(pwd) pipenv run pytest -s -rx -k $(K) --pdb store ./tests/ || true
