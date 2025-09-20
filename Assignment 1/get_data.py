def download_data(force=False):
    """Download and extract course data from Zenodo."""
    import urllib.request, zipfile, os
    
    zip_path = 'data.zip'
    data_dir = 'data'
    
    if not os.path.exists(zip_path) or force:
        print("Downloading course data")
        urllib.request.urlretrieve(
            'https://zenodo.org/records/16954427/files/data.zip?download=1',
            zip_path
        )
        print("Download complete")
    else:
        print("Download file already exists")
        
    if not os.path.exists(data_dir) or force:
        print("Extracting data files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print("Data extracted")
    else:
        print("Data directory already exists")

# -------------------
# Your analysis goes here
# -------------------
if __name__ == "__main__":
    download_data()

    import pandas as pd
    import numpy as np

    # Load dataset
    df = pd.read_csv("data/mn_police_use_of_force.csv")

    # -------------------
    # Your analysis goes here
    # -------------------

    print("\n====================")
print("VARIABLE: age (numeric)")
print("====================")
if "age" in df.columns:
    print("Type: Numeric")
    print("Missing values:", int(df["age"].isna().sum()))
    # ensure numeric (coerce just in case)
    age_num = pd.to_numeric(df["age"], errors="coerce")
    print(age_num.describe())
else:
    print("Column 'age' not found.")

print("\n====================")
print("VARIABLE: force_type (categorical)")
print("====================")
if "force_type" in df.columns:
    print("Type: Categorical")
    print("Missing values:", int(df["force_type"].isna().sum()))
    print("\nCounts:")
    print(df["force_type"].value_counts(dropna=False))
    print("\nProportions:")
    print(df["force_type"].value_counts(normalize=True, dropna=False).round(3))
else:
    print("Column 'force_type' not found.")

print("\n====================")
print("VARIABLE: race (categorical)")
print("====================")
if "race" in df.columns:
    print("Type: Categorical")
    print("Missing values:", int(df["race"].isna().sum()))
    print("\nCounts:")
    print(df["race"].value_counts(dropna=False))
    print("\nProportions:")
    print(df["race"].value_counts(normalize=True, dropna=False).round(3))
else:
    print("Column 'race' not found.")

print("\n====================")
print("VARIABLE: problem (categorical)")
print("====================")
if "problem" in df.columns:
    print("Type: Categorical")
    print("Missing values:", int(df["problem"].isna().sum()))
    print("\nTop 15 problem types by count:")
    print(df["problem"].value_counts(dropna=False).head(15))
else:
    print("Column 'problem' not found.")