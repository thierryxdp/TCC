def  bolos(A,B,C):
    '''Calcula e retorna a quantidade máxima de bolos que
    João consegue fazer com os ingredientes que possui em
    casa, forneça como entradas as quantidades inteiras de
    xícaras de farinha de trigo (A), ovos (B) e colheres de
    sopa (C).'''
    a = A//2
    b = B//3
    c = C//5
    return min(a,b,c)