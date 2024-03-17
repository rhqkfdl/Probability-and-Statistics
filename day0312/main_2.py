"""
2024년 3월 12일
남경남
확률과통계
1,2장 과제
"""

import numpy as np

a = np.array([1,2,3,4,5])
print(a*2)

a = np.array([1,2,'A'])
print(a)

a = np.array([1,2,3.14])
print(a)

a = np.arange(0, 0.8, 0.2)
print(a)

a = np.arange(3)
print(a)

# a = np.tile(7, (2,2,2))
# print(a)
a = np.tile(7, 3)
print(a)

a = np.full(7, 3)
print(a)

a = np.zeros([2,3])
print(a)

a = np.array([1,2,3,4,5])
print(a[1:3])
a = np.array([[1,2,3,4,5],
[6,7,8,9,10]])
print(a[0,3])
print(a[1, 2:4])

