def acima_da_media(x):
    lista = x.sort()
    x1 = len(lista)
    y = int(sum(lista) / x1)
    y2 = lista.index(y)
    return y2