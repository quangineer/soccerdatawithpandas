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



# # SELECT * FROM data WHERE Club = "Juventus"
# Juventus_data = data[data.Club == "Juventus"]
for i in unique_club:
    unique_club_data = data[data.Club == i]
    unique_club_data_values = unique_club_data["Value"]
    unique_club_data_values_list = unique_club_data_values.tolist()
    Club_total_value = 0
    for value in unique_club_data_values_list:
        value = float(value.strip("€MK"))
        Club_total_value += value
        
    print (Club_total_value)
    
# # SELECT Value FROM data WHERE Club = "Juventus"
# Juventus_values = Juventus_data["Value"]
# # Convert Value to array
# Juventus_values_list = Juventus_values.tolist()
    # print (unique_club_data_values_list)
# # Calculate total value (strip characters then convert to float then add to total)
# JuventusTotalValue = 0
# for value in Juventus_values_list:
#     value = float(value.strip("€MK"))
#     JuventusTotalValue += value
# print (JuventusTotalValue)

     
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