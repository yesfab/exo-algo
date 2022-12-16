import numpy
import statistics
from tri_a_bulle_optimisé import tri_bulle_opti
from tri_bulle_normal import tri_bulle
from tri_insertion import tri_insertion
from tri_selection import tri_par_selection


def stat (min: int, max: int, step: int, nbr: int):

   for i in range(min, max + 1, step):
        for j in range(1, nbr + 1, 1):
            m = numpy.random.randint(10, size=(i))
            # Exercice 2 tri par sélection
            nb = len(m)
            for k in range(0, nb):
                minimum = k
                for l in range(k + 1, nb) :
                    if m[l] < m[minimum] :
                        minimum = l
                        counter = counter + 1
                if min is not k :
                    temp = m[k]
                    m[k] = m[minimum]
                    m[minimum] = temp
                    # Fin tri par sélection
            k.append(counter)
            counter = 0
        mean = statistics.mean(j)
        print(i, mean)

