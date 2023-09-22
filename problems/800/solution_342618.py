def total(lista, produtos):
    '''Dada uma lista de compras e um dicionário contendo o preço de cada produto,
    retorna o valor total dos itens da lista;
    list, dict -> float'''

    valor = 0

    for item in lista:
        if item in produtos:
            valor += produtos[item]

    return valor