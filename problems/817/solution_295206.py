def acima_da_media(lista):
    lista1 = lista
    lista1.sort()
    x1 = len(lista1)
    y1 = int(sum(lista1) / x1)
    y = lista1.index(y1)
    del(lista1[0:y1+1:])
    return lista1