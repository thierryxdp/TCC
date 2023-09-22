def total(lista,dicio):
    '''
    Funçao que recebe uma lista de compras e um dicionario contendo os
    preços de cada produto disponivel em determinada loja e retorna o
    valor total dos itens da lista que estiverem disponiveis nesta loja
    list, dict -> float
    '''
    import math
    total = 0
    for i in range(len(dicio)):
        for list[i] in dicio:
            if list[i] in dicio:
                total = total + dict.values(dicio[i])
    return round(total,2)