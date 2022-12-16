# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab): 
    # Parcours de 1 à la taille du tab
    affectation = 0
    comparaison = 0
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        affectation += 1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
                comparaison += 1
        tab[j + 1] = k
        affectation += 1

    operation = affectation + comparaison

    return tab,operation

#partie test
tab = [5, 3, 1, 4, 2]
print(tri_insertion([5, 3, 1, 4, 2, 10])) 

"""
PROCEDURE tri_Insertion ( Tableau t)
    n ← taille tableau t
    POUR i VARIANT DE 0 à n
        min ← i
        POUR j de i + 1 à n - 1
              si t[j] < t[min], alors min ← j
        FIN POUR
        si min ≠ i, alors échanger t[i] et t[min]
    FIN POUR
FIN PROCEDURE
"""