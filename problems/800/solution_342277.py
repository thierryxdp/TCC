def total (compras,precos):
    '''
        Função que recebe uma lista de compras e um dicionario contendo os produtos e seus preços de uma loja e retorna o valor total dos produtos da lista disponiveis na loja
        list,dict->float
    '''
    valor_retornado = []
    for i in range(len(compras)):
        if compras[i] in precos:
            list.append(valor_retornado,dict.get(precos,compras[i]))
    return round(sum(valor_retornado),2)