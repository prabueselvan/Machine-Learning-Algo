import pandas as pd

df = pd.DataFrame({
    "clean_email": ["win free prize", None, "meeting tomorrow"],
    "v1": ["spam", "ham", "ham"]
})

# df = df.dropna(subset=["clean_email"])

# df = df.dropna(subset=["clean_email"]).copy()

df_filtered = df.dropna(subset=["clean_email"]).copy()


df_filtered["v1"] = "test"

print("Filtered DataFrame:")
print(df_filtered)

# print("Original DataFrame:")
# print(df)