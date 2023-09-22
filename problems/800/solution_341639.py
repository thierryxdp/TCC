def total(compras, dicionario):
    x = 0
    y = []
    for preco in compras:
        if compras[x] in dicionario:
            
            x = x + 1
    return compras[x]