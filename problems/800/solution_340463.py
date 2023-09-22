def total(lista,dicionario):
    k = 0
    f = dict.keys(dicionario)
    g = 0
    while k < len(lista):
        if lista[k] in f:
            g = g + dict.get(dicionario,lista[k])
        k = k + 1
    g = str(g)
    if len(g)>15:
        g = float(g)
        g = round(g,1)
    g = float(g)
    return g