def acima_da_media(lista):
    y1 = sum(lista) // len(lista)
    lista1 = lista
    lista1.sort()
    y = range(lista1[0:y1])
    return y