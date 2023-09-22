def receita (2, 3, 5):
    '''2 = xícaras, 3 = ovos, 5 = colheres de leite'''
    return 2+3+5

def bolo (A, B, C):
    '''retorna a quantidade de bolos que Joãozinho poderá fazer com base na rceita'''
    import math
    return math.ceil((A+B+C)/10)