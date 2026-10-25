import pandas as pd

from src.data.preprocess import clean_batch

def process_dataset():
    print ("Script Started")
    df= pd.read_csv("data/raw/email_spam.csv",encoding="cp1252")
    print ("Dataset Loaded")
    texts= df["v2"].astype(str).str.lower()
    texts =texts.str.replace(r"https\S+"," ",regex=True)
    texts =texts.str.replace(r"[^a-zA-Z]"," ",regex=True)
    df["clean_email"] = clean_batch(texts)
    print ("Cleaning Completed")
    df.to_csv("data/processed/cleaned_emails.csv", index=False)
    # print ("columns are ",df.columns)
    print (df["v1"].value_counts())
    print ("File Saved")
