def acima_da_media(x):
    lista = x
    lista.sort()
    y = len(lista)
    y1 = sum(lista) // y
    y2 = lista.index(y1)
    if y2 == y:
        return 'ola'
    del(lista[0:y2+1])
    return lista