def uppCons(entrada):
    indice = 0
    res = ''
    while indice < len(entrada):
        if str.lower(entrada[indice]) in 'bcdfghjklmnpqrstxyz':
            res += str.upper(entrada[indice])
        else:
            res += entrada[indice]
        indice += 1
    return res