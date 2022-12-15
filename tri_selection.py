# Trouvez le minimum de la liste et placez-le à la fin de la section triée

def tri_par_selection(lst):
    for l in range(len(lst)):
        min_i = l
        for i in range(l, len(lst)):
            if lst[i] < lst[min_i]:
                min_i = i
        lst[l], lst[min_i] = lst[min_i], lst[l]

    return lst

print(tri_par_selection([2,7,1,0,8,1]))
assert tri_par_selection([5, 3, 1, 4, 2]) == [1,2,3,4,5]&