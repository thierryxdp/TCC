def total(lista_compras,produtos):
    '''
    função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja;
    list, dic -> float
    '''
	valor_total = 0
    t = 0
    for compra in produtos:
        if lista_compras[t] in produtos:
            valor_total = valor_total + produtos[compra]
    return valor_total