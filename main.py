import pandas as pd
# import os
path_to_file = "data.csv"
# user_cols = ["Ai-Di", "Nem", "Et"]
data = pd.read_csv(path_to_file, usecols=["ID","Name","Age","Nationality","Position"])

# print(str(data.head(3)))
# print (data.dtypes)

# print(data.head(100))
# motlanchoilon = data.head(100)

list_of_positions = (data["Position"].tolist())
A = []
for i in range(len(list_of_positions)):
    if list_of_positions[i] not in A:
        A.append(list_of_positions[i])
        i = i+1
# print (A)

print (set(list_of_positions))