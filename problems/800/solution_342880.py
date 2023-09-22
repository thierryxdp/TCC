def total(lista, precos):
    ''' recebe uma lista de compras e um dicionário com os preços de cada produto e retorna o valor total dos itens da lista desejados'''
    lista = []
    precos = dict()
    itens=0
    for itens in lista:
        if precos in lista[itens]:
            lista= lista + list(dict.values(precos))
            return precos