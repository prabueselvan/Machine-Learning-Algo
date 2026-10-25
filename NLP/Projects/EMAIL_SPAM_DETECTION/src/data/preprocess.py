import nltk
import re
import spacy
from nltk.corpus import stopwords

nlp =spacy.load("en_core_web_sm")

def clean_text(text):
    text =str(text).lower()
    text = re.sub(r"http://\s+", " ", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    doc =nlp(text)
    words = [t.lemma_ for t in doc if not t.is_stop]
    return " ".join(words)


def clean_batch(texts):
    cleaned=[]
    docs = nlp.pipe(
        texts,
        batch_size=50,
        disable=["parser", "ner"]   
    )

    for doc in docs:
        words = [t.lemma_ for t in doc if not t.is_stop]
        cleaned.append(" ".join(words))
    return cleaned


