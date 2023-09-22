def total(lista, produtos):
    valor = 0
    for i in lista:
        if i in produtos.keys():
            valor = valor + produtos[i]
    return valor