# Trouvez le minimum de la liste et placez-le à la fin de la section triée

def tri_par_selection(lst):

    affectation = 0
    comparaison = 0

    for l in range(len(lst)):

        min_i = l 
        affectation += 1
        for i in range(l, len(lst)):

            comparaison += 1
            if lst[i] < lst[min_i]:

                
                min_i = i
                affectation += 1 

        lst[l], lst[min_i] = lst[min_i], lst[l] 
        affectation += 3
    
    operation = affectation + comparaison

    return lst, operation

print(tri_par_selection([2,7,1,0,8,1, 23, 76, 35, 45]))
