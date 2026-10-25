import csv
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
QUARANTINE_FILE = PROJECT_ROOT / "data" / "quarantine" / "quarantine.csv"
INBOX_FILE = PROJECT_ROOT / "data" / "inbox" / "inbox.csv"
EMAIL_FIELDS = ["timestamp", "label", "email_text"]


def store_email(email_text: str, label: str) -> None:
    if label == "spam":
        file_path = QUARANTINE_FILE
    elif label == "ham":
        file_path = INBOX_FILE
    else:
        raise ValueError(f"Unsupported email label: {label}")

    file_path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not file_path.exists()

    with file_path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=EMAIL_FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "label": label,
                "email_text": email_text,
            }
        )


def quarantine_email(email_text: str, label: str) -> None:
    if label != "spam":
        raise ValueError("Only spam emails can be added to quarantine")
    store_email(email_text, label)


def get_emails(label: str) -> list[dict[str, str]]:
    if label == "spam":
        file_path = QUARANTINE_FILE
    elif label == "ham":
        file_path = INBOX_FILE
    else:
        raise ValueError(f"Unsupported email label: {label}")

    if not file_path.exists():
        return []

    with file_path.open("r", newline="", encoding="utf-8") as file:
        return list(reversed(list(csv.DictReader(file))))
