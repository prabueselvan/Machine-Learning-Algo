# Email Spam Detection

## Run the FastAPI dashboard

From this project directory, activate the existing virtual environment if needed
and start the application:

```bash
source .venv/bin/activate
uvicorn src.api.app:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) for the dashboard or
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the API
documentation. The model and vectorizer are loaded from `models/` relative to
the project, so the server can be started from another working directory too.

## Classification and storage

The dashboard sends email text to `POST /api/classify` as JSON:

```json
{"text": "Email text to classify"}
```

The response includes the predicted `label`, model `confidence`, and
`destination`. SPAM is appended to `data/quarantine/quarantine.csv`; HAM is
appended to `data/inbox/inbox.csv`. The dashboard's Overview, Quarantine, and
Inbox tabs read the stored classifications from the API.

The original `POST /predict` endpoint remains available and returns the same
classification response.
