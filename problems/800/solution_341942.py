def total(lista,catalog):
    """ Recebe uma lista contendo os itens de compra
    e um dicionario contendo o catálogo de preços, retorna
    o valor total dos itens que etejam na lista.
    list, dic --> float"""
    preco=0
    for produto in lista:
        if produto in catalog:
            valor=dict.get(catalog,prouto)
            preco=preco+valor  
    return preco