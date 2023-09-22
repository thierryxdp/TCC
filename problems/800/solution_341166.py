def total(lista, dicionario):
    y = 0
    for x in range(len(dicionario)):
        a = lista[y]
        y = y + dicionario[a]
    return y