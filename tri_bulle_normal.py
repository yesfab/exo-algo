def tri_bulle(tableau):

    comparaison = 0
    affectation = 0
    compteur = 0

    for i in range(len(tableau)):

        for j in range(0, len(tableau) - i - 1):

            comparaison += 1
            if tableau[j + 1] < tableau[j]:

                compteur+= 1

                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
                affectation += 3

    operation = affectation + comparaison

    return tableau, operation , compteur

print(tri_bulle([1, 2 ,3,  4 ,5 ,6,7,8,9,10]))
print(tri_bulle([10,9,8,7,6,5,4,3,2,1]))