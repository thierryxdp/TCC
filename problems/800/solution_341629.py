def total(compras, dicionario):
    x = 0
    y = []
    while x < len(compras):
        if compras[x] in dicionario:
            z = compras[x]
            y = list.append(y, compras[0])
        x = x + 1
    return sum(y)