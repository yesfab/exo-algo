def tri_bulle(tableau):

    affectation = 0
    comparaison = 0
    compteur = 0

    permutation = True
    passage = 0

    affectation += 1
    while permutation == True:

        permutation = False
        affectation += 1

        passage = passage + 1
        affectation += 1

        for en_cours in range(0, len(tableau) - passage):
            
            comparaison += 1
            if tableau[en_cours] > tableau[en_cours + 1]:

                compteur += 1
                
                permutation = True
                affectation +=1

                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = \
                tableau[en_cours + 1],tableau[en_cours]
                affectation += 1

    operation = affectation + comparaison

    return tableau, operation , compteur

print(tri_bulle([1, 2 ,3,  4 ,5 ,6,7,8,9,10]))
print(tri_bulle([10,9,8,7,6,5,4,3,2,1]))

