"""
2024년 3월 15일
확률과통계
남경남
1,2장 9 ~ 14번까지 과제
"""

import numpy as np
import pandas as pd
# 9번
a = np.zeros(5, dtype=int)
print(a) # [0 0 0 0 0]

a = np.zeros((3,3), dtype=int)
print(a) # [[0 0 0] \n [0 0 0] \n [0 0 0]]

a = np.ones(5, dtype=float)
print(a) # [1. 1. 1. 1. 1.]

#10번
a = np.tile(5, 9)
print(a) # [5 5 5 5 5 5 5 5 5]

a = np.full(5, 9)
print(a) # [9 9 9 9 9]

a = np.eye(3, dtype=int)
print(a) # [[1 0 0] \n [0 1 0] \n [0 0 1]]

#11번
a = np.arange(20)
print(a) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(a.reshape(4,5)) # [[ 0  1  2  3  4] \n [ 5  6  7  8  9] \n [10 11 12 13 14] \n [15 16 17 18 19]]
print(a) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

#12번
a = [1,'A']
print(type(a[0])) # <class 'int'>
print(type(a[1])) # <class 'str'>

a = np.array(a)
print(type(a[0])) # <class 'numpy.str_'>
print(type(a[1])) # <class 'numpy.str_'>

#13번
df1 = pd.DataFrame({
 'a' : [1,2,3],
 'b' : [4,5,6]
 })
df2 = pd.DataFrame({
 'a' : [7,8,9],
 'b' : [10,11,12]
 })
cc = pd.concat([df1, df2], axis=0)
print(cc, '\n')
cc = pd.concat([df1, df2], axis=1)
print(cc, '\n')

#14번
a = pd.DataFrame(
 [['A', 1], ['B', 2], ['C', 3]],
 columns=['x1', 'x2']
 )
b = pd.DataFrame({
 'x1':['B','C','D'],
 'x3':[2,3,4] 
 }) 
print(a,'\n')
print(b,'\n')
print(pd.concat([a,b]), '\n')
print(pd.concat([a,b], axis = 1), '\n')