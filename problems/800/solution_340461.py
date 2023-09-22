def total(lista,dicionário):
    k = 0
    f = dict.keys(dicionário)
    g = 0
    while k < len(lista):
        if lista[k] in f:
            g = g + dict.get(dicionário,lista[k])
        k = k + 1
    return g