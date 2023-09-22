def total(lista,dicionario):
    k = 0
    f = dict.keys(dicionario)
    g = 0
    while k < len(lista):
        if lista[k] in f:
            g = g + dict.get(dicionario,lista[k])
        k = k + 1
    return g