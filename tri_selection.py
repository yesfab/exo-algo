# Trouvez le minimum de la liste et placez-le à la fin de la section triée

def tri_par_selection(lst):

    affectation = 0
    comparaison = 0
    compteur = 0

    for l in range(len(lst)):

        min_i = l 
        affectation += 1
        
        for i in range(l, len(lst)):

            comparaison += 1
            if lst[i] < lst[min_i]:

                compteur += 1

                min_i = i
                affectation += 1 

        lst[l], lst[min_i] = lst[min_i], lst[l] 
        affectation += 3
    
    operation = affectation + comparaison

    return lst, operation, compteur

print(tri_par_selection([1, 2 ,3,  4 ,5 ,6,7,8,9]))
print(tri_par_selection([9,8,7,6,5,4,3,2,1]))
