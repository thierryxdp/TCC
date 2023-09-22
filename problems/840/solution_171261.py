def receita (A=2, B=3, C=5):
    '''A = xícaras, B = ovos, C = colheres de leite'''
    return A+B+C

def bolo (A, B, C):
    '''quantidade não exata de bolos que Joãozinho poderá fazer'''
    return (A+B+C)/10

def bolos (A, B, C):
    '''quantidade exata de bolos que Joãozinho poderá fazer'''
    import math
    math.ceil(A+B+C)/10
    return (A+B+C)/10