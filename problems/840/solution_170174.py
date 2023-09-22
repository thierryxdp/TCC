import math
#ex. 3
def bolos(A, B, C):
    '''determine qual a quantidade maxima de bolos que o João consegue fazer, dados A = xícaras de farinha de trigo, B = ovos e C = colheres de sopa de leite'''
    return math.floor(min(A/2, B/3, C/5))