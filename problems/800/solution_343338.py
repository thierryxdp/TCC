def total(lista_compras,precos):
    '''
    função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja;
    list, dic -> float
    '''
	valor_total = 0.0
    for produto in precos:
        if produto in precos:
            valor_total = valor_total + precos[produto]
    return valor_total