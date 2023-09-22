def total(lista_compras,precos):
    '''
    função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja;
    list, dic -> float
    '''
	valor_total = 0.0
    for t in precos:
        if lista_compras[t] in precos:
            valor_total = valor_total + precos[lista_compras[t]]
    return valor_total