from math import floor
def bolos(a=2, b=3, c=5):
    ''' função que calcula e retorna a quantidade de bolos que pode ser feita por João sabendo que a quantidade mínima dos ingredientes para que um bolo possa ser feito é 2a, 3b e 5c '''
    return floor(a+b+c)//(2+3+5)