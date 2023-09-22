def bolos(A,B,C):
    '''função que dado a quantidade dos ingredientes A=2,B=3 e C=5,
    nessa proporção, calcula a quantidade máxima de bolos'''
    return min(A//2,B//3,C//5)