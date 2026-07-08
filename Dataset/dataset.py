import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("Titanic.csv")
print(df.info())
print(df.describe())

df["Age"]= df["Age"].fillna(df["Age"].median())
df["Embarked"]= df["Embarked"].fillna(df["Embarked"].mode()[0])

df= df.drop_duplicates()

first_class= df[df["Pclass"] == 1]
print("First class \n", first_class.head())

survival_rate= df.groupby("Pclass")["Survived"].mean()
survival_rate.plot(kind="bar", color="skyblue")
plt.title("Survival rate vs Class")
plt.xlabel("Class")
plt.ylabel("Survival rate")
plt.show()

sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="pink")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

