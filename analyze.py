from sklearn.metrics import accuracy_score
import pickle
import numpy as np
clf = pickle.load(open('knn.pkl','rb'))

with open('test.txt', 'r+') as f:
    data_test = f.readlines()
X_test = []
Y_test = []
for p in data_test:
    path = 'train/'+p
    X_test.append(np.load(path.strip('\n'))[0])
    Y_test.append(p.split('.')[0])
Y_pre = clf.predict(X_test)

print(accuracy_score(Y_test,Y_pre))
