import pandas as pd
import matplotlib .pyplot as plt # from matplotlib import pyplot as plt 같은 의미
plt.rcParams['font.family'] = 'Malgun Gothic' # 한글 깨짐을 고쳐줌, 폰트를 직접 지정해준다.

x = ['딸기', '바나나', '수박', '멜론', '복숭아', '자두']
y = [16109, 41401, 53121, 59899, 53450, 82565]

plt.bar(x, y)
plt.title('number of cases by month')
plt.show()