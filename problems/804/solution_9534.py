def filtra_pares(tupla):
    ind0 = tupla[0]%2
    ind1 = tupla[1]%2
    ind2 = tupla[2]%2
    ind3 = tupla[3]%2
    tuplapares = ()
    if ind0 == 0:
        tuplapares = (ind0)
    return tuplapares