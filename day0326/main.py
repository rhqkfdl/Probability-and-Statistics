import pandas as pd
import matplotlib .pyplot as plt # from matplotlib import pyplot as plt 같은 의미

data = pd.read_csv("C:/Users/ngn/Documents/VScode/확률과통계/day0326/file/중학생_남자_키/중학생_남자_키.csv")
# data type은 데이터 프레임이다. (<class 'pandas.core.frame.DataFrame'>)
plt.hist(data, label = 'bins=10', bins = 10)
plt.legend()
plt.show()

plt.hist(data, label = 'bins=5', bins = 5)
plt.legend()
plt.show()