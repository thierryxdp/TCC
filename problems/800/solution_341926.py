def total(compra,preco):
    '''Recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível
    em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis
    nesta loja.
    list,dict->float
    '''
    conta=0
    for x in range(len(compra)):
        if compra[x] in dicio.keys():
            conta+=dicio[compra[x]]
    return round(conta,2)