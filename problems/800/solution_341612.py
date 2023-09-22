def total(lista, precos):
    lista_compras = 0
    for produto in lista:
        if lista(produto) in precos:
            lista_compras = precos[produto]
    return lista_compras