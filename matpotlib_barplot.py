from matplotlib.ticker import FuncFormatter 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = "data.csv"
data = pd.read_csv(file)

club = set(data.Club)
unique_club = []
list_total_value_club = []
for i in club:
    if str(i) != "nan":
        unique_club.append(i)



# # SELECT * FROM data WHERE Club = "Juventus"
# Juventus_data = data[data.Club == "Juventus"]
for i in unique_club:
    unique_club_data = data[data.Club == i]
    unique_club_data_values = unique_club_data["Value"]
    unique_club_data_values_list = unique_club_data_values.tolist()
    Club_total_value = 0
    for value in unique_club_data_values_list:
        if value.endswith("K"):
            value = float(value.strip("€K"))*0.001
        elif value.endswith("M"):
            value = float(value.strip("€M"))
        else:
            value = 0 
        Club_total_value += value
    Club_total_value = round(Club_total_value, 2)
    list_total_value_club.append([i, Club_total_value])

S = sorted(list_total_value_club, key=lambda x: x[1])
# print (S)

A = S[-5:]
# print (A)
Club_Name = []
Club_Value = []
for i in A:
    Club_Name.append(i[0])
    Club_Value.append(i[1])
# print (Club_Name)
# print (Club_Value)


x = np.arange(5)
money = Club_Value


def millions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fM' % (x * 1e-6)


formatter = FuncFormatter(millions)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
plt.bar(x, money)
plt.xticks(x, (Club_Name))
plt.show()