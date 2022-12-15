def tri_bulle(tableau):

    permutation = True
    passage = 0

    while permutation == True:

        permutation = False
        passage = passage + 1

        for en_cours in range(0, len(tableau) - passage):

            if tableau[en_cours] > tableau[en_cours + 1]:
                
                permutation = True

                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = \
                tableau[en_cours + 1],tableau[en_cours]

    return tableau

print(tri_bulle([2,7,1,0,8,1]))
