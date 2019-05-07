import pandas as pd


filedata = 'data.csv'

#Read File :
data = pd.read_csv(filedata)

#Make an object out of an object:
data_Age = data["Age"]

#Make a list from object of data["Age"] from object of data:
# data_Age = data["Age"].tolist()

#Use python to find out how many players' age equal and over 30:
# A = []
# for i in range(len(data_Age)):
#     if data_Age[i] >= 30:
#         A.append(data_Age[i])    
# print (len(A))

#Shorter verion of the operation above:
# B = 0
# for i in range(len(data_Age)):
#     if data_Age[i] >= 30:
#         B += 1
# print (B)

#print how many columns and how many row in each column (does not count cell without any values)
# print (data.count())

#print how many row in columns Age
# print (data_Age.count())

#given the condition of Age >= 30, find out how many players in data file using SQL:
#This SQL count include every columns counts 
# print ((data[data.Age >= 30]).count())

#Using SQL to count: First select only column Age (of table data) where Age >= 30, then start counting
#For this SQL count, have to decide which column , which condition first to narrow the result, then using index of 
#data file to start counting.
# print ((data[data.Age >= 30])["Age"].count())

########################
#which player under 30 get paid the most?
#Remember: to strip an object, we use .item()
#SELECT Name
#From data
#Where Age < 30
#Order by Salary DESC,
#Limit 1 
print (data[data.Age < 30].sort_values('Value',ascending = False)["Name"][0:1].item())

#########################
#which player has the most potential but get paid the least?
