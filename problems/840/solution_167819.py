def bolos(A,B,C):
    '''computa a quantidade máxima possível de bolos'''
    #receita para 1 bolo: A=2, B=3 e C=5
    return min(A//2,B//3,C//5)