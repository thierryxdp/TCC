def total(compras, dicionario):
    x = 0
    y = []
    for preco in compras:
        if compras in dicionario:
            y = list.append(y, dicionario[compras[x]])
            x = x + 1
    return sum(y)