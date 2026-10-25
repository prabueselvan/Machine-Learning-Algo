# Step 1:
# from src.data.load_data import load_data

# df = load_data("data/raw/Reviews.csv")
# print(df.head())
# print (df.columns)


# Step 2:
# from src.data.load_data import load_data
# from src.data.preprocess import create_sentiment

# df = load_data("data/raw/Reviews.csv")

# df["sentiment"]= df["reviews.text"].apply(create_sentiment)

# print (df[["reviews.text", "sentiment"]].head())

# print("Available columns:", df.columns.tolist())


# Step 3:
# from src.data.preprocess import clean_text, clean_batch

# sample = """This product is amazing!!! I bought 2 units."""
# print (clean_text(sample))

# Step 4:
from src.data.process_dataset import process_dataset
process_dataset()