def uppCons(j):
    frase = ''
    i = 0
    while i<0:
        if j[i] in 'bcdfghjklmnpqrstvwxyz':
            frase = frase + str.upper(j[i])
        if j[i] not in 'bcdfghjklmnpqrstvwxyz':
            frase = frase + str.upper(j[i])
        i = i + 1
    return frase