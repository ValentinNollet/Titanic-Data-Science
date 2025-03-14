# Titanic-Data-Science
## **Analyse des données du Titanic pour voir quels facteurs ont influencé la survie des passagers. J'ai exploré les impacts du sexe, de l'âge et de la classe avec des visualisations sympas !**

🛳️

### **Exploration :**
**J'ai d'abord commencé par explorer le data set grâce à [ce code :](exploration.py)<br>**<br>

Ce code permet de :  
✔️ Afficher les 5 premières lignes du dataset  
✔️ Vérifier le nombre de lignes et de colonnes  
✔️ Identifier les valeurs manquantes  
✔️ Connaître le type des données  

Voici l'output du code : ![Exploration](Exploration%20.png)

On remarque donc que : <br>
- Le DataSet contient 891 lignes et 12 colonnes.<br>
- Le DataSet contient 3 Types de données différentes : Int64, float64 et object.<br>
- L'âge moyen à bord du titanic est de 29,7ans, le tarif moyen des billets est de 32,20, majorité des passagers se situe en 3ème classe...<br>
- Le DataSet contient des valeurs manquantes telles que l'âge (177 valeurs manquantes), Cabin (204 valeurs sur 891), Embarked (2 valeurs manquantes).<br>

<br>

### **Valeurs Manquantes :**
**J'ai donc par la suite, comblé les valeurs manquantes grâce à [ce code :](vmanquantes.py).<br>**

🔹 Âge : Remplacé par la médiane de l’âge des passagers de la même classe.  
🔹 Cabine : Valeurs manquantes remplacées par "Unknown".  
🔹 Embarquement : Les 2 valeurs manquantes remplacées par le port d’embarquement le plus fréquent. <br>  

Après ces corrections, le dataset ne contient plus de valeurs manquantes.

![Vmanquantes](vmanquantes.png)

<br>

### **Analyse**

**Une fois les données propres, j'ai pu analyser celles-ci grâce à [ce code :](Analyse.py).**<br>

Voici les graphiques obtenues : <br> 

![1](Répartition%20des%20survivants.png)
![2](Survie%20en%20fonction%20de%20sex.png)
![3](Survie%20en%20fonction%20de%20la%20classe.png)
![4](Survie%20en%20fonction%20de%20l'age.png)
![5](Décès%20en%20fonctionn%20de%20l'age.png)  

- Graphique 1 : On Remarque donc bien plus de décès que de survivants.
- Graphique 2 : Les femmes ont eu un taux de survie bien plus élevé que les hommes, et donc la majorité des hommes n'ont pas survécu.
- Graphique 3 : Les passagers de la 1ère classe ont le plus haut taux de survie. en 2ème classe, le taux de survie est plus équilibré entre surviants et non-survivants. En 3ème classe, il y a eu beaucoup plus de décès que de survivants. Cela nous montre que la classe sociale a eu un impact important. 
- Graphique 4-5 : Pour les survivants ont retrouve des pics à 1ans / 25ans / 35ans. Pour les non-survivants il y a une certaines homogénéité mais on retrouve un pics vers 25ans.


### Conclusion
Cette analyse montre que le sexe, la classe sociale et l’âge ont eu une influence significative sur la survie des passagers du Titanic.










  
