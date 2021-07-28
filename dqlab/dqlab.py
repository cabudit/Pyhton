import pandas as pd
# import dataset
df = pd.read_csv(
    "customer_segments.txt", sep="\t")

# menampilkan data
print(df)
