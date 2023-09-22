def total(lista,produtos):
    '''função que retorna o valor total dos itens da lista que estejam disponíveis nesta loja, dada uma lista de compras e um dicionário contendo o preço
    dos produtos disponíveis em uma loja, 
    list, dict --> float '''
    lista1 = list(produtos)
    preco = 0
    for produto in lista:
        if produto in lista1:
            preco = preco + produtos[lista1[list.index(lista1,produto)]]
    return round(preco,2)