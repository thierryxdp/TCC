def bolos(A,B,C):
    '''
    função que calcula a quantidade máxima de bolos que é possível fazer com A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite
    '''
    import math
    farinha = math.floor(A/2)
    ovos = math.floor(B/3)
    leite = (C/5)
    return math.floor(farinha,ovos,leite)