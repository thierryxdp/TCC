def total(compras, dicionario):
    x = 0
    y = []
    z = dicionario[compras[0]]
    while x < len(compras):
        if compras[x] in dicionario:
            y = list.append(y, z)
            x = x + 1
    return sum(y)