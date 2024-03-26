import matplotlib .pyplot as plt # from matplotlib import pyplot as plt 같은 의미

x = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
y1 = [14.4, 14.5, 15.4, 16.9, 17.8, 17.6, 27.6]
y2 = [20.5, 21.0, 22.8, 23.6, 24.2, 24.3, 29.5]

plt.plot(x, y1, linestyle = 'solid', label = 'teens')
plt.plot(x, y2, linestyle = 'dashed', label = '20s')

plt.legend(loc = 'best', ncol = 2)

plt.title('Internet Usage Time per Week')
plt.show()