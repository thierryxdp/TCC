def filtra_pares(a,b,c,d):
    lista=tuple()
    lista2=(a,b,c,d)
    lista=filter(lambda x: x%2 == 0,lista2)
    return lista