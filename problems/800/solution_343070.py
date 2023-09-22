def total(lista, dicionario):
    preco = 0
    for x in lista:
        if x in dicionario:
            preco = preco + dicionario[x]
        else:
            preco = preco
    return round(preco, 2)