# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
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
    
    numero = []
    for produto in lista:
        if dict.get(cardapio, produto, 0) != 0:
            list.append(numero, dict.get(cardapio, produto))
    return round(sum(numero), 2)