def acima_da_media(x):
    lista = x
    lista.sort()
    y = len(lista)
    y1 = sum(lista) // y
    y2 = lista.index(y1)
    return del(lista[0:y2+1])