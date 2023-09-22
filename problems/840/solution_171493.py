def bolos (A, B, C):
    '''retorna a quantidade máxima de bolos que Joãozinho poderá fazer
    dados A as xícaras, B os ovos e C as colheres'''
    return min(A//2, B//3, C//5)