import os
import numpy as np
from sklearn.feature_selection import VarianceThreshold
x = []
feature_name = []
# read raw features
with open('../data/features.csv') as f:
    first_line = f.readline()
    first_line = first_line.rstrip(os.linesep)
    first_line = first_line.split(',')
    feature_name = first_line[1:]
    for line in f:
        x.append([])
        temp = line.rstrip(os.linesep)
        temp = temp.split(',')
        temp = temp[1:]
        for i in temp:
            if i == '':
                x[-1].append(np.nan)
            else:
                x[-1].append(float(i))
    f.close()
x = np.array(x)
x = x.astype('float32')
feature_name = np.array(feature_name)
# remove features with any nan value
isnan = ~np.isnan(x).any(axis=0)
x = x[:,isnan]
feature_name = feature_name[isnan]
# remove features with any infinite value
isinf = ~np.isinf(x).any(axis=0)
x = x[:,isinf]
feature_name = feature_name[isinf]
# remove features with any negative infinite value
isneginf = ~np.isneginf(x).any(axis=0)
x = x[:,isneginf]
feature_name = feature_name[isneginf]
# remove features with zero variance
sel = VarianceThreshold()
x = sel.fit_transform(x)
feature_name = feature_name[sel.get_support()]
# output the data
with open('../data/features_clean.csv','w') as f:
    f.write(','.join(feature_name))
    f.write(os.linesep)
    for i in range(len(x)):
        temp = []
        for v in x[i]:
            temp.append(str(v))
        f.write(','.join(temp))
        f.write(os.linesep)
    f.close()
