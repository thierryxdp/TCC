def bolos(A,B,C):
    '''funcao que calcula a quantidade de bolos que joao pode fazer com os ingredientes que possui'''
    trigo = (A//2)
    ovos = (B//3)
    leite = (C//5)
    return min(triho,ovos,leite)