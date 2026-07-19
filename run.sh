source .venv/bin/activate
uvicorn main:app --env-file .env --reload
