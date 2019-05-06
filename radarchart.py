import pandas as pd 
import matplotlib.pyplot as plt 
from math import pi

soccerfile = "data.csv"
# data = pd.read_csv(soccerfile, usecols=["Finishing", "SprintSpeed", "Acceleration","Balance","Strength",""])
data = pd.read_csv(soccerfile)

Player_ID = int(input("Please enter player identification number:"))

Player_Name = (data[data.ID == Player_ID].Name).item()
Player_Strength = float(data[data.ID == Player_ID].Strength)
Player_Attacking = float(data[data.ID == Player_ID].Finishing)
Player_Balance = float(data[data.ID == Player_ID].Balance)
Player_Speed = ((float(data[data.ID == Player_ID].SprintSpeed)+float(data[data.ID == int("20801")].Acceleration))/2)
Player_Defending = ((float(data[data.ID == Player_ID].StandingTackle)+float(data[data.ID == int("20801")].SlidingTackle))/2)
# Player_KPI = [Player_Attacking, Player_Balance, Player_Defending, Player_Speed, Player_Strength]
# print (Player_KPI)

df = pd.DataFrame({
'group': [Player_Name],
'Attack': [Player_Attacking],
'Defensiveness': [Player_Defending],
'Balance': [Player_Balance],
'Speed': [Player_Speed],
'Strength': [Player_Strength]
})


categories=list(df)[1:]
N = len(categories)


values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values

angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]


ax = plt.subplot(111, polar=True)

plt.xticks(angles[:-1], categories, color='grey', size=8)


ax.set_rlabel_position(0)
plt.yticks([20,50,80], ["20","50","80"], color="grey", size=7)
plt.ylim(0,100)

ax.plot(angles, values, linewidth=1, linestyle='solid')

ax.fill(angles, values, 'b', alpha=0.1)

plt.title(Player_Name)

plt.show()