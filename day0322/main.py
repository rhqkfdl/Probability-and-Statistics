import numpy as np

h = np.loadtxt("C:/Users/ngn/Documents/VScode/Probability-and-Statistics/day0322/file/중학생_남자_키.txt")
print(h.size) # 4933
print(h.mean()) # 160.2737482262315
print(h.std()) # 7.8374814853952826

# z-score : 내키 - 평균키 / 표준편차
a = (168-h.mean()) / h.std()
print(f"a = {a}") # 0.83646	
b = 100-(0.8364 * 100)
print(b)

# 마지막 확인문제
# 17.04
# 16.35