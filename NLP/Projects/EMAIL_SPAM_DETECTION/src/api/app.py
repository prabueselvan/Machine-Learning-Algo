from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from src.data.preprocess import clean_text
from src.quarantine.store import get_emails, store_email

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL = joblib.load(PROJECT_ROOT / "models" / "spam_model.pkl")
VECTORIZER = joblib.load(PROJECT_ROOT / "models" / "count_vectorizer.pkl")

app = FastAPI(title="Email Spam Detection", version="1.0.0")


class Email(BaseModel):
    text: str = Field(min_length=1, max_length=100_000)


def classify_email(email_text: str) -> dict[str, str | float]:
    cleaned_email = clean_text(email_text)
    features = VECTORIZER.transform([cleaned_email])
    label = str(MODEL.predict(features)[0]).lower()

    confidence = 1.0
    if hasattr(MODEL, "predict_proba"):
        probabilities = MODEL.predict_proba(features)[0]
        predicted_index = list(MODEL.classes_).index(label)
        confidence = float(probabilities[predicted_index])

    if label not in {"spam", "ham"}:
        raise HTTPException(status_code=500, detail=f"Unexpected model label: {label}")

    store_email(email_text, label)
    return {
        "label": label,
        "confidence": confidence,
        "destination": "quarantine" if label == "spam" else "inbox",
    }


@app.get("/", include_in_schema=False)
def dashboard() -> FileResponse:
    return FileResponse(PROJECT_ROOT / "src" / "api" / "static" / "index.html")


@app.get("/api/emails/{folder}")
def list_folder_emails(folder: str) -> list[dict[str, str]]:
    if folder not in {"inbox", "quarantine"}:
        raise HTTPException(status_code=404, detail="Folder not found")
    return get_emails("ham" if folder == "inbox" else "spam")


@app.get("/api/overview")
def overview() -> dict[str, int]:
    inbox_count = len(get_emails("ham"))
    quarantine_count = len(get_emails("spam"))
    return {
        "inbox": inbox_count,
        "quarantine": quarantine_count,
        "total": inbox_count + quarantine_count,
    }


@app.post("/api/classify")
@app.post("/predict", include_in_schema=False)
def predict(email: Email) -> dict[str, str | float]:
    return classify_email(email.text)
