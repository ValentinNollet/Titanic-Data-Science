import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("titanic.csv")

df["Age"].fillna(df.groupby("Pclass")["Age"].transform("median"), inplace=True)
df["Cabin"].fillna("Unknown", inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

sns.countplot(x="Survived", data = df)
plt.title("Répartition des survivants")
plt.ylabel("Valeur")
plt.show()

sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survie en fonction du sexe")
plt.ylabel("Valeur")
plt.show()

sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Survie en fonction de la classe")
plt.ylabel("Valeur")
plt.show()

sns.histplot(df[df["Survived"] == 1]["Age"], bins=30, color="green", label="Survivants")
plt.legend()
plt.title("Survie en fonction de l'age")
plt.ylabel("Valeur")
plt.show()


sns.histplot(df[df["Survived"] == 0]["Age"], bins=30, color="red", label="Non survivants")
plt.legend()
plt.title("Décès en fonction de l'age")
plt.ylabel("Valeur")
plt.show()