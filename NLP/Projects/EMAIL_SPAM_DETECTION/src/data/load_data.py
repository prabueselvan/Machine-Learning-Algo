import pandas as pd

def load_data(file: str):
    return pd.read_csv(file, encoding="cp1252")