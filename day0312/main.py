"""
2024년 3월 12일
남경남
확률과통계
pandas를 이용한 파일 읽기를 실습한 내용
"""
import pandas as pd
import os
import openpyxl

file_df = pd.read_csv("C:/Users/ngn/Documents/VScode/Python_Script/day0312/file/sample1.csv")
print(file_df)

file_df2 = pd.read_csv("C:/Users/ngn/Documents/VScode/Python_Script/day0312/file/sample2.txt",encoding="UTF-8")
print()
print(file_df2)

file_df3 = pd.read_csv("C:/Users/ngn/Documents/VScode/Python_Script/day0312/file/sample3.txt",sep='\t',encoding="UTF-8")
print()
print(file_df2)

file_df4 = pd.read_excel("C:/Users/ngn/Documents/VScode/Python_Script/day0312/file/sample4.xlsx")
print()
print(file_df4)