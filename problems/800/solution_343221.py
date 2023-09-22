def total (lista,precos):
    ''' Função que recebe uma lista de compras e um dicio contendo
    os pordutos e seu preços disponiveis em uma determinada loja, e
    retorna o valor total dos itens da lista que estejam disponíveis nesta loja
    list,dicio -> int '''

    total = 0
    for produto in lista:
        if produto in precos:
            total= total + (dict.get(precos,produto))
    return round(total,2)