def uppCons(entrada):
    indice = 0
    res = ''
    while indice < len(entrada):
        if entrada[indice] in 'aeiouAEIOU':
            res += entrada[indice]
        else:
            res += str.upper(entrada[indice])
        indice += 1
    return res