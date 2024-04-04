import pandas as pd

def read_csv_file() :
# Define the file path
    file_path = "WRAP.csv"

# Read the CSV file into a DataFrame
    df = pd.read_csv(file_path, sep=";", header=None)

# Print the DataFrame
    df_subset = df.iloc[6:15]
    dates = df_subset.iloc[:,0]
    bostadsbidrag = df_subset.iloc[:,2]

#print(df_subset)
#print(dates)
#print(bostadsbidrag)

    data = list(zip(dates,bostadsbidrag))

    return data