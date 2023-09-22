def total(lista_compras,preco_produto):
    '''
    função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível e retorna o valor total dos itens da lista que estejam disponíveis na loja;
    list, dic -> float
    '''
    valor_total = 0
    for produto in lista_compras:
        if produto in preco_produto:
            valor_total = valor_total + preco_produto[produto]
    return valor_total