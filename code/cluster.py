from __future__ import print_function
import pandas as pd
import sklearn.metrics as met
from sklearn import preprocessing
from sklearn.cluster import DBSCAN

preprocess = 'std'

print('citanje podataka...', end='')
df = pd.read_csv("datasets/backup2_preimenovano.csv")
print('gotovo')
features = df.columns[1:12].tolist()
x_original=df[features]

print('Preprocesiranje podataka...', end='')
# Preprocesiranje
if preprocess == 'std':
    x=pd.DataFrame(preprocessing.scale(x_original))
elif preprocess == 'norm':
    x=pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(x_original))
else:
    x = x_original
print('gotovo')

# Dodeljivanje imena kolonama
x.columns = features

print('features:', features)

print('=-----------------------------------------=')
print('=              klasterovanje              =')
print('=-----------------------------------------=')
for eps in range(1, 21):
    for min_samples in range(0, 201, 10):
        if min_samples == 0:
            min_samples = min_samples + 1
        print("eps:", eps)
        print("min_samples:", min_samples)
        est=DBSCAN(eps=eps*0.1, min_samples=min_samples)
        est.fit(x)
        col_name = 'labels_' + str(eps) + '_' + str(min_samples)
        df[col_name]= est.labels_
        num_clusters=max(est.labels_)+1
        print("number of clusters:", num_clusters)
        print('=-----------------------------------------=')

df.to_csv('datasets/clustered_data.csv')

