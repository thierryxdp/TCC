def total(compras, dicionario):
    x = 0
    y = []
    z = compras[x]
    while x < len(compras):
            y = list.append(y, dicionario[z])
            x = x + 1
    return sum(y)