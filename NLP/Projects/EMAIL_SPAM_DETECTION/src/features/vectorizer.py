
import pandas as pd
import joblib

from sklearn.feature_extraction.text import CountVectorizer

# Load processed dataset
df = pd.read_csv("data/processed/cleaned_emails.csv")

# Check missing values
print("Missing emails:", df["clean_email"].isna().sum())

# Remove rows with missing email text
df = df.dropna(subset=["clean_email"]).copy()

print (df.head())

# Ensure email text is string
df["clean_email"] = df["clean_email"].astype(str)

# Initialize CountVectorizer
vectorizer = CountVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

# Convert text into numerical features
X = vectorizer.fit_transform(df["clean_email"])



# Save vectorizer
# joblib.dump(vectorizer, "models/count_vectorizer.pkl")

# print("Vectorized shape:", X.shape)
# print("Vectorizer saved successfully!")
