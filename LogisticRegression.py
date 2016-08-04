#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

import os
import operator
import numpy as np
from numpy import loadtxt
import sklearn
from sklearn import linear_model

data = loadtxt('LR_FeatureFile.txt')
#	print data
labels = loadtxt('LR_LabelFile.txt')
#	print labels
clf = sklearn.linear_model.LogisticRegression(tol=0.0001, fit_intercept=True, intercept_scaling=1, solver='liblinear', max_iter=500, multi_class='ovr')
clf.fit(data, labels)
testdata = loadtxt('LR_TestFile.txt')
h = clf.predict(testdata)
hideal = loadtxt('LR_TestLabels.txt')
size = '%s' %str(h.shape)
pstr = size[1:-2]
count = float(pstr)
print h
diff = h-hideal
error = float(np.count_nonzero(diff))
accuracy = float((count-error)/count)
result = '\n Accuracy of Logistic Regression = '
result+= '%f' %float(accuracy)
print result + '\n \n'
exit()
