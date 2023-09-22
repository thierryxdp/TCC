def total(lista, dicionario):
    produtos = str.split(lista)
    preco = 0
    for e in produtos:
        d = dicionario[e]
        preco = preco + d
    return preco