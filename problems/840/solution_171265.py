def receita (A=2, B=3, C=5):
    '''A = xícaras, B = ovos, C = colheres de leite'''
    return A+B+C

def bolo (A, B, C):
    '''quantidade não exata de bolos que Joãozinho poderá fazer'''
    return A/2, B/2, C/2

def bolos (A, B, C):
    '''quantidade exata de bolos que Joãozinho poderá fazer'''
    import math
    math.floor(A+B+C)/bolo
    return (A+B+C)/bolo