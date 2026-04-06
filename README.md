Projet Python – Algorithmes de base

Description
Projet personnel en Python portant sur la manipulation de listes numériques, le calcul de statistiques simples, l’implémentation de tris et la recherche de valeurs, sans utiliser les fonctions intégrées de Python.

Contenu
-minimum, maximum, moyenne (sans utiliser les fonctions disponibles)
-tri par insertion et tri fusion
-recherche linéaire et dichotomique
-lecture de données depuis un fichier CSV

Choix techniques
-tri par insertion pour les listes de petite taille (moins de 30 éléments)
-tri fusion pour les listes plus grandes
-recherche dichotomique uniquement sur liste triée

Utilisation
data = lire_csv("data.csv")
print(analyse(data))

valeur = int(input("Valeur à rechercher : "))
print(recherche(data, valeur))

Structure
analyseur_de_donnee.py
data.csv
README.md

Contexte
Projet réalisé dans une démarche de préparation à une entrée en L2 Informatique.