#!/usr/bin/python

# -*- coding: utf-8 -*-

import ClustersSource

blognames,words,data=ClustersSource.readfile('Blog Data.txt')

print('Iteration Count:')

kclust=ClustersSource.kcluster(data, k = 5)

print('K-Means Values:')
print(kclust)

print(' ')

print('K-Means Clusters (k = 5):')
for i in range(0, 5):
    print(str(i + 1) + ': '  + str([blognames[r] for r in kclust[i]]))
    print(' ') 