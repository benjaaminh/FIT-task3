import pandas as pd


#the data is reversed in comparison to api data, so we reverse the list
def reverse(lst):
    new_lst = lst[::-1]
    return new_lst

def read_csv_file() :
#define the file path
    file_path = "WRAP.csv"

#read the CSV file into a DataFrame
    df = pd.read_csv(file_path, sep=";", header=None)

#pick out the necessary data values
    df_subset = df.iloc[6:15]

#pick out the right column from the subset
    bostadsbidrag = df_subset.iloc[:,2]

#make a list of it
    data = list(bostadsbidrag)
#reverse it so it fits with the other data
    reversed = reverse(data)
    return reversed