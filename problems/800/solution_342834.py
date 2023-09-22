def total(lista, cardapio):
    '''
    função que recebe uma lista de compras e um dicionario
    contendo o preço de cada produto disponível de uma
    determinada loja, e retorna o valor total dos itens da lista
    que estejam disponíveis.
    :param lista: list
    :param cardapio: dict
    :return: float
    '''
    
    disponiveis = []
    for produto in lista:
        if dict.get(cardapio, produto, 0) != 0:
            list.append(disponiveis, dict.get(cardapio,produto,0)
    return round(sum(disponiveis),2)