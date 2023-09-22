def total(compras, dicionario):
    x = 0
    y = []
    z = compras[x]
    while x < len(compras):
        if compras[x] in dicionario:
            y = list.append(y, dicionario[z])
        x = x + 1
    return sum(y)