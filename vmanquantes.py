import pandas as pd 

df = pd.read_csv("titanic.csv")

df["Age"].fillna(df.groupby("Pclass")["Age"].transform("median"), inplace=True)
df["Cabin"].fillna("Unknown", inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)


print(df.info())
