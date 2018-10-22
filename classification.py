import imp
import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pickle
X_train = []
Y_train = []

with open('train.txt', 'r+') as f:
    data_train = f.readlines()

print('aa')
print(len(data_train))
for p in data_train:
    path = 'train/'+p
    X_train.append(np.load(path.strip('\n'))[0])
    Y_train.append(p.split('.')[0])

print('done prepare data')

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, Y_train)
print('done train')
pickle.dump(neigh,open('knn.pkl','wb'))
