def total(lista, dicionario):
    y = 0
    x = 0
    for x in range(len(dicionario)):
        a = lista[x]
        y = y + dicionario[a]
    x = x + 1
    y = y + 1    
    return y