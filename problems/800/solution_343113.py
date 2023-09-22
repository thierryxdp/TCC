def total(lista,dicionario):
    '''recebe uma lista de compras e um dicionário
    contendo o preço de cada produto disponível em
    uma determinada loja e retorna o valor dos itens
    da lista que estejam disponíveis nesta loja.
    list,dict -> float
    '''
    valor = 0
    for produto in dicionario:
        valor += dicionario[produto]
    return round(valor,2)