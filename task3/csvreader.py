import pandas as pd

# Define the file path
file_path = "WRAP.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, sep=";")

# Print the DataFrame
df_subset = df.iloc[5:14]

print(df_subset)
