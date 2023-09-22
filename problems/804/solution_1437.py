def filtra_pares(a,b,c,d):
    lista1 = (a,b,c,d)
    lista2 = sorted(filter(lambda x: x% 2 == 0, lista1))
    return lista2