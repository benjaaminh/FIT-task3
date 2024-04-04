import pandas as pd

# Define the file path
file_path = "WRAP.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, sep=";")

# Print the DataFrame
print(df)
