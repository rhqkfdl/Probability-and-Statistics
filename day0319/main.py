import numpy as np
# 15번 확인문제
# 표본분산 : 데이터들이 평균에서 얼마나 멀리 떨어져있는지를 나타내는 값
# 표본분산 공식 : https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmPKoq%2FbtqDQT3XZkK%2F75C7z2oGrMyWAb4XseTqxk%2Fimg.png
# 불편분산 : 편중되지않은 분산
# 불편본산 공식 : https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FG1CoQ%2FbtqDSiPhF58%2FtfxyYPBowTkCxrWUF0jj9K%2Fimg.png

# 16번 확인문제
fish = np.array([2,3,3,4,4,4,4,5,5,6])
print('분산 :', fish.var(), np.var(fish))
print('불편분산 :', fish.var(ddof=1), np.var(fish, ddof=1))
print('표준편차 :', fish.std(), np.std(fish))
print('불편표준편차 :', fish.std(ddof=1), np.std(fish, ddof=1))

#17번 확인문제

# 정규화 : 데이터를 특정 범위로 변환하여 범위를 일치시키는 것
# 표준화 : 평균 : 0, 표준편차 : 1 변환하여 데이터를 바꾸는 것
# 정규화 결과 : [0.   0.25 0.25 0.5  0.5  0.5  0.5  0.75 0.75 1.  ]
# 표준화 결과 : [-1.82574186 -0.91287093 -0.91287093  0.          0.          0.          0.          0.91287093  0.91287093  1.82574186]

# 18번 확인문제
fish_I = (fish - fish.min()) / (fish.max() - fish.min())
print(f"정규화 결과 : {fish_I}")

fish_II = (fish - fish.mean()) / fish.std()
fish_II_round = np.round(fish_II.mean(), 5)
print(f"표준화 결과 : {fish_II}")
print(f"평균 : {fish_II_round}")
print(f"표준편차 : {fish_II.std()}")
# print(f"분산 : {fish_II.var()}")
