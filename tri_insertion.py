# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k

#partie test
tab = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(tab) 
print ("Le tableau trié est:")
for i in range(len(tab)): 
    print ("% d" % tab[i])

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