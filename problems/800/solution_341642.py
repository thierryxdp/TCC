def total(compras, dicionario):
    x = 0
    y = []
    while x < len(compras):
        if compras[x] in dicionario:
            y = y + [dicionario[compras[x]]]
            
        x = x + 1
    return y