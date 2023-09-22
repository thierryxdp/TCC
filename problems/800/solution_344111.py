def total(listadecompras,precodosprodutos):
    '''Retorna o valor total dos itens da lista de compras a partir
    dos preços dos produtos disponíveis em uma loja
    entrada:list, dictionary
    saída:float
    '''
    precototal=0
    for produto in listadecompras:
        if produto in list(dict.keys(precodosprodutos)):
            precototal=precototal+precodosprodutos[produto]
    precototal=round(precototal,2)
    return precototal