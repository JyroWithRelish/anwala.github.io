import NumPredict
import math
import re

file = open('Blog Data.txt')
data = []
for line in file: 
  line = line.strip()
  data.append([int(x) for x in line.split('\t')])
vectorA = data[0]
vectorB = data[1] 

print('Results for vectorA:')
result = NumPredict.knnestimate(data, vectorA, 1)
print('kNN estimate of k = 1: ' + str(result))

result = NumPredict.knnestimate(data, vectorA, 2)
print('kNN estimate of k = 2: ' + str(result))

result = NumPredict.knnestimate(data, vectorA, 5)
print('kNN estimate of k = 5: ' + str(result))

result = NumPredict.knnestimate(data, vectorA, 10)
print('kNN estimate of k = 10: ' + str(result))

result = NumPredict.knnestimate(data, vectorA, 20)
print('kNN estimate of k = 20: ' + str(result))

print(' ')

print('Results for vectorB:') 
result = NumPredict.knnestimate(data, vectorB, 1)
print('kNN estimate of k = 1: ' + str(result))

result = NumPredict.knnestimate(data, vectorB, 2)
print('kNN estimate of k = 2: ' + str(result))

result = NumPredict.knnestimate(data, vectorB, 5)
print('kNN estimate of k = 5: ' + str(result))

result = NumPredict.knnestimate(data, vectorB, 10)
print('kNN estimate of k = 10: ' + str(result))

result = NumPredict.knnestimate(data, vectorB, 20)
print('kNN estimate of k = 20: ' + str(result))