import math
import re

'''
Original Code: https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter8/numpredict.py
'''

def cosine(vec1,vec2):
    'compute cosine similarity of vec1 to vec2: (vec1 dot vec2)/{||vec1||*||vec2||)'
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(0, 958):
        x = vec1[i]; y = vec2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)


def getdistances(data,vec1):
  distancelist=[]
  
  # Loop over every item in the dataset
  for i in range(len(data)):
    vec2=data[i]
    
    # Add the distance and the index
    distancelist.append((cosine(vec1,vec2)))
  
  # Sort by distance
  distancelist.sort()
  return distancelist

def knnestimate(data,vec1,k):
  # Get sorted distances
  dlist=getdistances(data,vec1)
  avg=0.0
  
  # Take the average of the top k results
  for i in range(k):
    idx=dlist[i]
    avg+=dlist[i]
  avg=avg/k
  return avg
