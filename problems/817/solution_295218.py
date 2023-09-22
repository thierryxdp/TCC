def acima_da_media(x):
    lista = x
    lista.sort()
    y = len(lista)
    y1 = sum(lista) // y
    if y1 not in lista:
        y2 = lista.index(y1)
        return del(lista[-1:y1])
    y2 = lista.index(y1)-1
    del(lista[0:y2+2])
    return lista