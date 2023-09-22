def acima_da_media(x):
    lista = x
    lista.sort()
    y = len(lista)
    y1 = sum(lista) // y
    y2 = lista.index(y1)-1
    if y < y2:
        return 'oi '
    del(lista[0:y2+2])
    return lista