from math import floor
def bolos(a, b, c):
    ''' função que calcula e retorna o máximo de bolos que Jaão consegue fazer com (a) xícaras de farinha de trigo, (b) ovos e (c) colheres de sopa de leite ''' 
    return floor((a*2+b*3+c*5)/10)