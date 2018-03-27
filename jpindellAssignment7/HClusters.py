#!/usr/bin/python

# -*- coding: utf-8 -*-

import ClustersSource

blognames,words,data=ClustersSource.readfile('Blog Data.txt')

clust=ClustersSource.hcluster(data)

ClustersSource.printclust(clust, labels=blognames)

ClustersSource.drawdendrogram(clust,blognames,jpeg='Blog Cluster.jpg') 