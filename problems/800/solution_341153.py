def total(lista,dicio):
    '''
        dada uma lista de compras e um dicionário de produto-preço, retorna o total
        da compra.
        list,dict -> int
    '''
    compras = 0
    for el in lista:
        if el in dicio:
            compras= compras + dicio[el]
    return compras