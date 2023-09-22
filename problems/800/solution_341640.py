def total(compras, dicionario):
    x = 0
    y = []
    while x < len(compras):
        if compras[x] in dicionario:
            y = y + 2
            
        x = x + 1
    return y