from math import *
#Questão 1.3
def bolos(a,b,c):
    '''calcula o número de bolos que João consegue fazer com "a" xícaras de farinha de trigo, "b" ovos e "c" colheres de sopa de leite'''
    return min(a//2,b//3,c//5)