def total(lista,dicionario):
    '''
    recebe uma lista de compras e um dicionario contendo o preço de caa profuto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loa;
    list, dict -> float
    '''
	produto = 0
    for produto in lista:
        if lista[produto] in dicionario[produto]:
            compras = dicionario[produto]
        compras = compras + dicionario[produto] + 1
    produto = produto + 1
    return compras