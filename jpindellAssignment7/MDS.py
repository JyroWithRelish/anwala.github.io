#!/usr/bin/python

# -*- coding: utf-8 -*-

import ClustersSource

blognames,words,data=ClustersSource.readfile('Blog Data.txt')

coords=ClustersSource.scaledown(data)

ClustersSource.draw2d(coords,blognames,jpeg='Blog MDS.jpg') 