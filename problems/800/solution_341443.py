def compras(item, di_mercado):
    ''' Função que recebe uma lista de compras com 3 itens e um dicionário 
        contendo o preço de cada produto disponível em uma determinada loja, 
        e retorna o valor total dos itens da lista que estejam disponíveis nesta loja.
        : param item: list
        : param di_mercado: dict
        : return: float
    '''
    x= item[0]
    y= item[1]
    z= item[2]
    if (item[0] in di_mercado) and (item[1] in di_mercado) and (item[1] in di_mercado):
        return di_mercado[item[0]] + di_mercado[item[1]] + di_mercado[item[2]]
    elif (item[0] in di_mercado) and (item[1] in di_mercado):
        return di_mercado[item[0]] + di_mercado[item[1]]
    elif (item[0] in di_mercado) and (item[2] in di_mercado):
        return di_mercado[item[0]] + di_mercado[item[2]]
    elif (item[1] in di_mercado) and (item[2] in di_mercado):
        return di_mercado[item[1]] + di_mercado[item[2]]
    elif item[1] in di_mercado:
        return di_mercado[item[1]]
    elif item[2] in di_mercado:
        return di_mercado[item[2]]
    elif item[0] in di_mercado:
        return di_mercado[item[0]]