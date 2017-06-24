from __future__ import print_function
import pandas as pd
import sklearn.metrics as met
from sklearn import preprocessing
from sklearn.cluster import DBSCAN

df = pd.read_csv("datasets/backup2_preimenovano.csv")

#prikaz imena kolona + 5 prvih instanci
print('Prvih 5 instanci', df.head(), sep='\n')
print('\n\n')

features = df.columns[1:12].tolist()
x_original=df[features]

#bez preprocesiranja
#x = x_original

#standardizacija atributa
x=pd.DataFrame(preprocessing.scale(x_original))

#normalizacija
#x=pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(x_original))

#dodeljivanje imena kolonama
x.columns = features

"""
Density-Based Spatial Clustering of Applications with Noise

parametri:

eps : maksimalna udaljenost za instance-komsije
      default:0.5
min_samples : broj suseda koje mora da ima instanci u jezgru
      default:5
metric : metrika za racunanje rastojanja
      default:'euclidean'

atributi:

core_sample_indices_ : indeksi instanci u jezgru

components_ : kopija instanci u jezgru
labels_ : oznake klastera za svaku instancu. Instance koje se smatraju sumom imaju
oznaku -1
"""

for eps in range(3, 8):
    for min_samples in range(2, 4):
        est=DBSCAN(eps=eps*0.1, min_samples=min_samples)
        est.fit(x)
        df['labels']= est.labels_
        num_clusters=max(est.labels_)+1

