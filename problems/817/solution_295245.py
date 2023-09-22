def acima_da_media(lista):
    y1 = sum(lista) // len(lista)
    lista1 = lista + [y1]
    lista1.sort()
    if y1 not in lista1:
        y = sum(lista1)//len(lista1)
        return lista1[y:] 
    y = lista1.index(y1)
    del(lista1[0:y+2])
    return lista1