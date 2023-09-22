def total(lista,produtos):
    '''Dada uma lista de compras e um dicionário contendo o preço
    dos produtos disponíveis em uma loja, retorna o valor total
    dos itens da lista que estejam disponíveis nesta loja
    list, dict -> float '''
    l1 = list(produtos)
    preco = 0
    for produto in lista:
        if produto in l1:
            preco = preco + produtos[l1[list.index(l1,produto)]]
    return round(preco,2)