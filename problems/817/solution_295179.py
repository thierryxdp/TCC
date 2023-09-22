def acima_da_media(x):
    lista = x.sort()
    x1 = len(x)
    y = int(sum(x) / x1)
    y2 = lista.index(y)
    return y2