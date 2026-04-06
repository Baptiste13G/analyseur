# Analyseur de données – Python

## Description
Projet personnel en Python portant sur l'implémentation from scratch d'algorithmes fondamentaux appliqués à des listes numériques : statistiques, tri et recherche, sans recourir aux fonctions intégrées de Python (min, max, sorted).

## Fonctionnalités
- Calcul du minimum, maximum et moyenne
- Tri par insertion (listes ≤ 30 éléments) et tri fusion (listes > 30 éléments)
- Recherche linéaire et dichotomique (sélection automatique selon la taille)
- Lecture de données depuis un fichier CSV

## Utilisation
```python
data = lire_csv("data.csv")
print(analyse(data))

valeur = int(input("Valeur à rechercher : "))
print(recherche(data, valeur))
```

## Structure
```
analyseur_de_donnee.py
data.csv
README.md
```

## Contexte
Projet réalisé en autonomie dans le cadre d'une préparation à une entrée en L2 Informatique, visant à consolider les bases algorithmiques.