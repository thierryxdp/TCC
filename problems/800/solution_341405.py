def total(lista,produtos):
    '''Dada uma lista de compras e um dicionário contendo o preço
    dos produtos disponíveis em uma loja, retorna o valor total
    dos itens da lista que estejam disponíveis nesta loja
    list, dict -> float '''
    lista = list(produtos)
    preco = 0
    for produto in lista:
        if produto in lista:
            preco = preco + produtos[lista[list.index(lista,produto)]]
    return round(preco,2)