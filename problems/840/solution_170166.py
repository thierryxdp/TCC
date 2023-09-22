import math
def bolos(A,B,C):
    '''Calcula a quantidade máxima de bolos que podem ser feitos, dados os valores de A,B,C que são xícaras de farinha de trigo, ovos e colheres de sopa de leite, respectivamente'''
    return (math.ceil(math.ceil(A/2))+(math.ceil(B/3))+(math.ceil(C/5)))/3