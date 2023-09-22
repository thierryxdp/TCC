def filtra_pares(tupla):
    a = []
    for n in range(len(tupla)):
        if tupla[n]%2 == 0:
            a.append(tupla[n])
    a = tuple(a)
    return(a)