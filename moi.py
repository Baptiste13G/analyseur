def recherche_valeur(tab : list[int]):
    """Cette fonction demande à l'utilisateur une valeur et la recherche dans la base de données en donnant son indice. Recherche linéaire"""
    indice=-1
    while True:
        try:
            recherche = int(input("Quelle valeur souhaitez-vous rechercher ? "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    if len(tab)==0:
        print("La liste donnée en paramètre est vide.")
    for i in range(len(tab)):
        if tab[i] == recherche:
            indice=i+1
    if indice == -1:
        print("La valeur que vous avez rentrée n'est pas dans la liste.")
    else:
        print(f"La valeur que vous avez rentrée :  {recherche}  est à l'indice n°{indice}")

def recherche_dicho(tab: list[int]):
    """Recherche une valeur dans une liste triée par recherche dichotomique."""
    tab_t = tri(tab)
    n = len(tab_t)
    while True:
        try:
            recherche = int(input("Quelle valeur souhaitez-vous rechercher ? "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    debut = 0
    fin = n - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if tab_t[m] == recherche:
            print(f"La valeur recherchée {recherche} est à l'indice {m+1}")
            return
        elif recherche > tab_t[m]:
            debut = m + 1
        else:
            fin = m - 1
    print("La valeur n'est pas présente dans la liste.")