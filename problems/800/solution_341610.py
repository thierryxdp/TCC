def total(compras, dicionario):
    x = 0
    y = []
    for preco in compras:
        if compras[x] in dicionario:
            y = list.append(y, dicionario[compras[0]])
            x = x + 1
    return sum(y)