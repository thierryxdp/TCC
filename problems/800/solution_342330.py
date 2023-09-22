def total(lista,dicionario):
    '''
    recebe uma lista de compras e um dicionario contendo o preço de caa profuto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loa;
    list, dict -> float
    '''
    a = 0
    for compras in lista:
        if lista[a] in dicionario:
            compras = dicionario[lista[a]]
        a = a + compras
    return compras