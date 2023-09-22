def total(c, p):
    '''Retorna o valor total da lista de compras.
    list, dict -> float'''
    acc = 0
    for i in range(len(c)):
        acc + = p[c[i]]
    return acc