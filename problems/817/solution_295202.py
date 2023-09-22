def acima_da_media(lista):
    lista1 = lista
    lista1.sort()
    y1 = sum(lista1)
    y = lista1.index
    del(lista1[0:y+1])
    return lista1