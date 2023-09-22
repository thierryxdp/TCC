def acima_da_media(lista):
    y1 = sum(lista) // len(lista)
    lista1 = lista + [y1]
    lista1.sort()
    return lista1