from math import*
def bolos (a,b,c):
    '''função que gera a quantiade máxima de bolos que joão pode fazer com (a) xícaras de farinha,(b) ovos e (c) colheres de sopa de leite; int, int, int -> float'''
    return a//gcd(a,b)