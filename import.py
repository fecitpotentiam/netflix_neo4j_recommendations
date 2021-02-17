import pandas as pd

dataframe = pd.read_csv('data/netflix_titles.csv')

print(dataframe.columns)

for index, row in dataframe.iterrows():
    print(row['cast'])