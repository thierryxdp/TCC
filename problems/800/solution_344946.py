def total(lista, produtos):
    valor = 0
    p = dict.keys(produtos)
    for i in lista:
        if i in p:
            valor += produtos[i]
    return round(valor, 2)