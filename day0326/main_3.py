import pandas as pd
import matplotlib .pyplot as plt # from matplotlib import pyplot as plt 같은 의미
plt.rcParams['font.family'] = 'Malgun Gothic' # 한글 깨짐을 고쳐줌, 폰트를 직접 지정해준다.

ratio = [22, 24, 16, 38]
labels = ['피자', '햄버거', '파스타', '치킨']

plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()