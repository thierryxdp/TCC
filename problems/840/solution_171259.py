def receita (x = 10):
    '''2 = xícaras, 3 = ovos, 5 = colheres de leite'''
    return x

def bolos (A, B, C):
    '''retorna a quantidade de bolos que Joãozinho poderá fazer com base na rceita'''
    import math
    return math.ceil(A+B+C)/receita