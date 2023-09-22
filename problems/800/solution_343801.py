def total(lista, dicionario):
    preco = 0
    for e in lista:
        d = dicionario[e]
        preco = preco + d
    return preco