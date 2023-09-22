def filtra_pares(a,b,c,d):
    lista=[a,b,c,d]
    lista2=sorted(filter(lambda x: x%2 == 0, lista))
    return lista2