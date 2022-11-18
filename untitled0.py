# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 21:29:51 2022

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv('fandango_score_comparison.csv')
file.head(20)
film_name = file['FILM']
Metacritic_users = file['Metacritic_user_vote_count']
IMDB_users = file['IMDB_user_vote_count']
Fandango_users = file['Fandango_votes']
Fandango_users.head(2)
plt.figure(figsize= (10,4))
plt.plot(file.loc[:,'FILM'],Fandango_users,color="red", label="Fandango_votes")
plt.plot(file.loc[:,'FILM'],Metacritic_users,color="brown", label="Metacritic_user_vote_count")
plt.plot(file.loc[:,'FILM'],IMDB_users,color = "blue" , label="IMDB_user_vote_counts")
plt.xticks(rotation=90)
plt.grid(linewidth=1)
plt.legend()
plt.xlabel("Names")
plt.ylabel("votes")
plt.title("scores comparison between different online movies websites")
plt.show()
file = pd.read_excel('report.xlsx')
file.head()
#creating a new file and seperating the data
n_f = file['Expense Type'].value_counts().rename_axis('Expense_Type').reset_index(name='count')
print(n_f)
n_f.loc[:,"Expense_Type"]
#creating our pie chart
fig = plt.figure()
y_explode = [0,0,0,0.05,0.1,0.1]
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(n_f.loc[:,"count"],labels=n_f.loc[:,"Expense_Type"],autopct='%.2f',explode=y_explode)
plt.title('HEath and safety expenses')
plt.legend(loc='upper left',prop={'size': 8})
file = pd.read_csv('movies.csv')
file.head(2)
estimated_budget = file['budget']
final_budget =file['budget_2013$']
final_domgross =file['domgross_2013$']
estimated_domgross =file['domgross']
final_intgross =file['intgross_2013$']
estimated_intgross =file['intgross']
plt.scatter(final_budget,estimated_budget,color='blue',s=100,label='budget',marker='.')
plt.scatter(final_domgross,final_intgross,color='red',s=100,label='final profits',marker='.')
plt.scatter(estimated_domgross,estimated_intgross,color='green',s=100,label='estimated profits',marker='.')
plt.grid()
plt.xlabel('total_budget')
plt.ylabel('estimated_budget')
plt.legend()
plt.title('budget analysis of movies 2013')
plt.figure(figsize= (6,3))

