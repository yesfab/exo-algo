def tri_à_bulles_optimise(Tableau: T):
    for i in (len.T)-1 < 1:
        tableau_trié := True
        for j in 0 < i-1:
            if T[j+1] < T[j]:
                (T[j+1], T[j]) = (T[j], T[j+1])
                tableau_trié := False
        if tableau_trié
    		return Tableau T

print(tri_à_bulles_optimise([2,7,1,0,8,1]))
assert tri_à_bulles_optimise([5, 3, 1, 4, 2]) == [1,2,3,4,5]

def triABulles(Tableau: t):
	for i in range(t)-1 < 1:
    	for j in 0 < i-1:
        	if t[j+1] < t[j]:
            	(t[j+1], t[j]) = (t[j], t[j+1])
			return Tableau t

print(triABulles([2,7,1,0,8,1]))
assert triABulles([5, 3, 1, 4, 2]) == [1,2,3,4,5]