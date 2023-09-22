from math import floor
def bolos(a, b, c):
    ''' função que calcula e retorna o máximo de boloa que Jaão consegue fazer com (a) xícaras de farinha de trigo, (b) ovos e (c) colheres de sopa de leite ''' 
    return floor(2*a+3*b+5*c)