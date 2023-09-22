def acima_da_media(lista):
    y1 = sum(lista) // len(lista)
    lista1 = lista + [y1 + 1]
    lista1.sort()
    y = lista1.index(y1)
    if y not in lista:
        del(lista1[0:y+1])
        return lista1
    del(lista1[0:y+2])
    return lista1