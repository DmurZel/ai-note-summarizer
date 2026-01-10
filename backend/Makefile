run:
	lsof -t -i:8000 | xargs -r kill -9
	source venv/bin/activate && uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

kill:
	lsof -t -i:8000 | xargs -r kill -9

install:
	source venv/bin/activate && pip install -r requirements.txt

freeze:
	source venv/bin/activate && pip freeze > requirements.txt