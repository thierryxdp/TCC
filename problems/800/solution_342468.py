def total(produtos, listacompras):
    '''Recebe uma lista de compras  e um dicionario contendo o preco
    de cada produto, e retorna o valor total 
    dos itens da lista que a loja possui
    list, dict ---> dict '''
    listacompras = []
    produtos = {}
    total  = 0
    for listacompras in produtos:
        total = sum(produtos[listacompras])
        return round(total, 2)