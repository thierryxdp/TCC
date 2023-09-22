def bolos(A, B, C):
    '''a partir da farinha de trigo, ovos e leite, calcula quantas receitas integrais de bolo podem ser feitas'''
    farinha = A // 2
    ovos = B // 3
    leite = C // 5
    return min(farinha, ovos, leite)