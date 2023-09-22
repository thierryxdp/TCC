def acima_da_media(lista):
    lista1 = lista
    lista1.sort()
    x1 = len(lista1)
    y1 = sum(lista1) / x1
    y = lista1.index
    return lista1