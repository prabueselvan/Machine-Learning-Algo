import pandas as pd
import os
from src.data.preprocess import clean_text, clean_batch 
os.makedirs("data/processed", exist_ok=True)

def process_dataset():
    print ("Script started")
    df = pd.read_csv("data/raw/Reviews.csv")
    print ("Dataset Loaded")
    # Random sample, NOT head() — the file is grouped by product,
    #    # so the first rows are a narrow slice. random_state keeps it repeatable.
    print ("Total Rows", len(df))    
    df= df.sample(n=500, random_state=42)
    df["sentiment"] =df["reviews.text"].apply(clean_text)
    print ("Sentiment Created")
    texts =   df["reviews.text"].astype(str).str.lower()
    texts = texts.str.replace(r"http\S+", " ", regex=True)
    texts = texts.str.replace(r"[^a-zA-Z]"," ", regex=True)

    df["clean_review"]=clean_batch(texts)
    print ("Cleaned Review Created")
    df.to_csv("data/processed/cleaned_reviews.csv", index=False)
    print ("File Saved")


