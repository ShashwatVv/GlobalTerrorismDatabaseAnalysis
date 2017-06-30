import pandas as pd
from operator import itemgetter

data = pd.read_csv('datasets/clusters_corr.csv')
cols = [[data.columns[1]]]
cols.append(data.columns[13:].tolist())
cols = sum(cols, [])
data = data[cols]
data = data[~data['attr_name'].isin(['latitude', 'longitude'])]

lst1 = list(['attr_name'])
lst = list()
for i in data.columns[1:]:
    m = max(data[i], key=abs)
    lst.append(dict({'label': i, 'max': abs(m)}))

sorted_list = sorted(lst, key=itemgetter('max'), reverse=True)
for i in range(0,15):
    lst1.append(sorted_list[i]['label'])

print('Zanimljivi klasteri:')
print(lst1[1:])
print(data[lst1])

