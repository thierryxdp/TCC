def total(x,y):
    '''Esta função calcula o preço da lista de compras
    em determinado mercado
    assinatura: list, dict -> float'''
    soma = 0
    c = 0
    for c in range(len(x)):
        soma = soma + y[x[c]]
    return round(soma,2)