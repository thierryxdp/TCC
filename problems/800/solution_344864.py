def total(c, p):
    '''funçao dado um lista de compras e um dicionario com os produtos retorna o total gasto
    list, dic -> float'''
    t = 0
    for i in c:
        if i in p:
            t = t+p[i]
    return t