def total(c, p):
    '''Retorna o preço das compras pela lista de compras
    e pelo dicionário de produtos.
    list, dict -> float'''
    acc = 0
    for i in range(len(c)):
        acc += p[c[i]]
    return acc