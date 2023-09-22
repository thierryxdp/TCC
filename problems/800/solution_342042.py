def total(ls, d):
    '''Computa o custo de comprar
    os produtos desejados (especificados
    pela lista /ls/) usando os preços
    da tabela de preços contida em /d/'''
    custo = 0
    for p in ls:
        # Qual é o preço de p?
        custo = custo + d[p] # é o preço de p
    return custo