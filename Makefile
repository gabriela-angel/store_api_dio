# -----    RULES     -----
run:
	@echo "Starting the FastAPI server..."
	@uvicorn store_api.main:app --reload

precommit-install:
	@echo "Installing pre-commit hooks..."
	@pipenv run pre-commit install

test:
	@echo "Running tests with pytest..."
	-@PYTHONPATH=$PYTHONPATH:$(pwd) pipenv run pytest -v tests/ || true

# "m" is the message for the migration
create-migrations:
	@echo "Creating a new Alembic migration..."
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "$(m)"

run-migrations:
	@echo "Running Alembic migrations..."
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head
