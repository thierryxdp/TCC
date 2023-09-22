def acima_da_media(x):
    lista = []
    y = sum(x) / len(x)
    y1 = x.sort()
    y2 = y1.index(y)
    return y2