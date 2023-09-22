def uppCons(j):
    frase = j
    i = 0
    while i<0:
        if j[i] in 'bcdfghjklmnpqrstvwxyz':
            j = j + str.upper(j[i])
        if j[i] not in 'bcdfghjklmnpqrstvwxyz':
            j = j + str.upper(j[i])
        i = i + 1
    return j