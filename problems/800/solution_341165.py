def total(lista, dicionario):
    y = 0
    for x in range(len(dicionario)):
        y = y + dicionario[lista[y]]
    return y