from matplotlib.ticker import FuncFormatter 
import matplotlib.pyplot as pyplot
import numpy as numpy
import pandas as pd

file = "data.csv"
data = pd.read_csv(file)

club = set(data.Club)
unique_club = []
for i in club:
    if str(i) != "nan":
        unique_club.append(i)

print (unique_club)
# formatter = FuncFormatter(millions)

# x = np.arange(10)

# from matplotlib.ticker import FuncFormatter
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(4)
# money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]


# def millions(x, pos):
#     'The two args are the value and tick position'
#     return '$%1.1fM' % (x * 1e-6)


# formatter = FuncFormatter(millions)

# fig, ax = plt.subplots()
# ax.yaxis.set_major_formatter(formatter)
# plt.bar(x, money)
# plt.xticks(x, ('Bill', 'Fred', 'Mary', 'Sue'))
# plt.show()