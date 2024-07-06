import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
movies = pd.read_csv("movies.dat", delimiter='::',engine='python')
print(movies.head()) #it will display first 5 movie records
print("="*60)
movies.columns = ["ID", "Title", "Genre"]
print(movies.head()) #it will display first 5 movie records with specified column names
print("="*60)
ratings = pd.read_csv("ratings.dat", delimiter='::',engine='python')
print(ratings.head()) #it will display first 5 rating records
print("="*60)
ratings.columns = ["User", "ID", "Ratings", "Timestamp"]
print(ratings.head()) #it will display first 5 rating records with specified column names
print("="*60)
data = pd.merge(movies, ratings, on=["ID", "ID"]) #merge two dataframes by using common column name ID
print(data.head()) #it will display both first 5 movie & rating records
ratings = data["Ratings"].value_counts()
numbers = ratings.index
quantity = ratings.values

plt.pie(quantity,labels=numbers,shadow=True,autopct="%.2f%%")
plt.show()
print("="*60)
data2 = data.query("Ratings == 10")
print(data2["Title"].value_counts().head(10))
