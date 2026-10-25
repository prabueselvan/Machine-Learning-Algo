
import joblib
from src.data.preprocess import clean_text

model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/count_vectorizer.pkl")

while True:
    email = input("\nEnter your email (or type 'exit' to quit): ")

    if email.lower() == "exit":
        break

    cleaned_email = clean_text(email)

    X = vectorizer.transform([cleaned_email])

    prediction = model.predict(X)

    print("\nPrediction:", prediction[0])
