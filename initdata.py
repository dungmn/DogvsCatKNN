import os
import numpy as np
from random import shuffle

def createTrainTest(path,p):
    list_feat = os.listdir(path)
    l = int(len(list_feat)*p)

    shuffle(list_feat)
    train = list_feat[:l]
    test = list_feat[l:]
    with (open('train.txt','w+')) as f:
        for p in train:
            f.write(p+'\n')
    with (open('test.txt','w+')) as f:
        for p in test:
            f.write(p+'\n')aa
createTrainTest('vgg16_fc2',0.7)
