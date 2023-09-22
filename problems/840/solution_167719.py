import math
def bolos(a,b,c):
    '''função que calcula a quantidade máxima de bolos que João consegue fazer, A representa xícaras de farinha
    B ovos e c colheres de sopa de leite'''
    return min(math.floor(a/2),math.floor(b/3),math.floor(c/5))