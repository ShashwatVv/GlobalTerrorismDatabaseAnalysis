from __future__ import print_function
import pandas as pd

df = pd.read_csv("datasets/backup2_preimenovano.csv")

features = df.columns[0:12].tolist()
x=df[features]
x.columns = features

for index, row in x.iterrows():
    if len(row) != 12:
        print(row['id'], "=>", len(row))
    if row.isnull().any():
        print(row['id'], " has null")

