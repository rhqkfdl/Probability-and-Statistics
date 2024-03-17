"""
2024년 3월 15일
확률과통계
남경남
1,2장 수업진도
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'col1':[1,2,3,4,5],
    'col2':[2,4,6,8,10],
    'col3':['A','B','C','D','E']
})

print(df.query('index == 0')) # 1 2 A
print(df.query("col3 == 'B'")) # 2 4 B
#print(df.query("col3 == 'A' & col1 == 2")) # 오류
print(df.query('col3=="A" | col1==2')) # 1 2 A \n 2 4 8
print('-'*8)

a = df.col1
print(type(a)) # <class 'pandas.core.series.Series'>
a = np.array(df.col1)
print(type(a)) # <class 'numpy.ndarray'>
a = df.col1.values 
print(type(a)) # <class 'numpy.ndarray'>
