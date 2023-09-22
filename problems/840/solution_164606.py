import math as m
def bolos(A,B,C):
    '''calcula e retorna a quantidade de bolos que se pode fazer
    dado a quantidade de farinha A, ovos B, leite C
    int,int,int,->int'''
    return m.floor(min(A/2,B/3,C/5))