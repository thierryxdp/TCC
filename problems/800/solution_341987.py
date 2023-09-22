def total(lista, dicionario):
    n = 0
    for n in lista:
        n = n + dict.get(dicionario, n)
    return dict.get(dicionario, n)