def total(lista, precos):
    lista_compras = 0
    for produto in lista:
        if produto in precos:
            lista_compras = lista_compras + precos[produto]
    return round(lista_compras, 2)