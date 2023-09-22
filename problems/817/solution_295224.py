def acima_da_media(lista):
    y1 = sum(lista) // len(lista)
    lista1 = lista + [y1]
    lista1.sort()
    y = lista1.index(y1)
    del(lista1[0:y+2])
    return lista1