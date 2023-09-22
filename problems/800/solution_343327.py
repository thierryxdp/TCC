def total(lista_compras,precos):
    '''
    função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja;
    list, dic -> float
    '''
	valor_total = 0
    t = 0
    for produto in precos:
        if lista_compras[t] in precos:
            valor_total = valor_total + precos[produto]
        t = t + 1
    return valor_total