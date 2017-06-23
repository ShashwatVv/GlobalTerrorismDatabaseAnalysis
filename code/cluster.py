from __future__ import print_function
import pandas as pd
import sklearn.metrics as met
from sklearn import preprocessing
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

df = pd.read_csv("backup_preimenovano.csv")

#prikaz imena kolona + 5 prvih instanci
print('Prvih 5 instanci', df.head(), sep='\n')
print('\n\n')

featurs = df.columns[1:3].tolist()
x_original=df[featurs]

#standardizacija atributa
x=pd.DataFrame(preprocessing.scale(x_original))


exit()
#normalizacija
#x=pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(x_original))

#dodeljivanje imena kolonama
x.columns = featurs

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


colors = ['darkcyan', 'magenta', 'gold', 'blue', 'navy', 'green', 'red']

fig = plt.figure()

plt_ind=1
for eps in range(3, 8):
    for min_samples in range(2, 4):
        est=DBSCAN(eps=eps*0.1, min_samples=min_samples)
        est.fit(x)
        df['labels']= est.labels_
        num_clusters=max(est.labels_)+1

        fig.add_subplot(5,2,plt_ind)
        for j in range(-1,num_clusters):
            cluster= df.loc[lambda x: x['labels'] == j, :]
            #cluster= df.loc[lambda x: x['labels'] == j, 'height':'labels']

            #print(cluster)
            #print('\n\n\n')
            if j==-1:
                label='nois'
            else:
                label = "cluster %d" % j
            plt.scatter(cluster['height'], cluster['weight'], color=colors[j], s=10, marker='o', label=label)

        plt.legend(loc='lower right',fontsize=6)
        plt.title('DBSCAN, eps:%.2f, min samples: %d'%(eps*0.1, min_samples), fontsize=10)
        plt_ind+=1

plt.tight_layout()
plt.show()
