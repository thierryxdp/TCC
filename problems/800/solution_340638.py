def total(lista,dici):
    '''recebe uma lista de compras e um dicionário contendo o valor de cada produto disponível no mercado e retorna o valor total dos itens da lista disponiveis; list,dict->float'''
    resposta=0
    for mantimento in lista:
        a=dict.get(dici,mantimento,0)
        resposta=resposta+a
    return round(resposta,2)