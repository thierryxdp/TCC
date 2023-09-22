from math import ceil
def bolos(a,b,c):
    '''função que calcula o máximo de bolos que João consegue fazer com (a) xícaras de farinha de trigo, (b) ovos e (c) colheres de sopa de leite'''
    return ceil(2/a)+ceil(3/b)+ceil(5/c)