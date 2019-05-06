import pandas as pd
import os
import matplotlib.pyplot as plt


path_to_file = "data.csv"
# user_cols = ["Ai-Di", "Nem", "Et"]
# data = pd.read_csv(path_to_file, usecols=["ID","Name","Age","Nationality","Position", "Potential"])

# print(str(data.head(3)))
# print (data.dtypes)
# print(data.head(100))

data = pd.read_csv(path_to_file, usecols=["Age", "Weight"])
# print (data)

list_of_age = data["Age"].tolist()
list_of_weight = list(data["Weight"])

list_of_weight_wo_float = []
for i in list_of_weight:
        if str(i) != "nan":
                list_of_weight_wo_float.append(i)

for i in range(len(list_of_weight_wo_float)):
        list_of_weight_wo_float[i] = int(list_of_weight_wo_float[i].strip('lbs'))
# print (list_of_age)
# print (list_of_weight_wo_float)
# print (list_of_weight[0].strip('lbs'))

plt.plot([list_of_age], [list_of_weight_wo_float], 'ro')
plt.axis([0, 50, 0, 250])
plt.show()


# list_of_positions = (data["Position"].tolist())
# A = []
# for i in range(len(list_of_positions)):
#     if list_of_positions[i] not in A:
#         A.append(list_of_positions[i])
#         i = i+1
# B = []
# for i in A:
#         if str(i) != "nan":
#                 B.append(i)

# print (B)

# print (data.dtypes)
# print (data["Potential"].tolist())
# print (set(list_of_positions))


# plt.subplot(2, 1, 1)
# plt.plot(data["Age"].tolist(), data["Potential"].tolist(), 'bo')
# plt.xlabel('Age')       
# plt.ylabel('Potential')
# # plt.show()


# AgePotentialArray = []
# for i, j in zip(data["Age"].tolist(), data["Potential"].tolist()):
#         AgePotentialArray.append([i,j])
# # print(AgePotentialArray)

# AgePotentialDict = dict()
# for age, potential in AgePotentialArray:
#         if age not in AgePotentialDict:
#                 AgePotentialDict[age] = []
#         AgePotentialDict[age].append(potential)

# for key, value in AgePotentialDict.items():
#         AgePotentialDict[key] = sum(value) / len(value)

# print(AgePotentialDict)
# plt.subplot(2, 1, 2)
# plt.plot(list(AgePotentialDict.keys()), list(AgePotentialDict.values()), 'bo')
# plt.xlabel('Age')       
# plt.ylabel('Potential')
# plt.show()

