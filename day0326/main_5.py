import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("C:/Users/ngn/Documents/VScode/확률과통계/day0326/file/초등학생_키몸무게/초등학생_키몸무게.xlsx")

plt.scatter(data.height, data.weight)

plt.xlabel('height')
plt.ylabel('weight')

plt.show()