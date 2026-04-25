import pandas as pd
import glob
import os

os.makedirs("output", exist_ok=True)

files = glob.glob("data/*.csv")

dfs = []

for file in files:
    df = pd.read_csv(file)

    df.columns = df.columns.str.strip()
    
    df = df[df["product"].str.lower() == "pink morsel"]

    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

    df["Sales"] = df["price"] * df["quantity"]

    df = df[["Sales", "region", "date"]]

    dfs.append(df)

if dfs:
    final_df = pd.concat(dfs, ignore_index=True)
    final_df.to_csv("output/pink_morsels_sales.csv", index=False)
    print("Processing complete! File saved to output/pink_morsels_sales.csv")
else:
    print("No data found or no files matched the criteria.")