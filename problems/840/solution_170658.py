import math
def bolos (A,B,C):
    '''funcao que dados os parametros a,b,c que indicam respectivamente o número de xicaras de farinha de trigo, o numero
    de ovos e o numero de colheres de sopa de leite que joao tem em casa, deve retornar a quantidade maxima de bolos que joão
    consegue fazer
    int,int,int->int'''.
    return min (math.floor (A/2), math.floor (B/3), math.floor (C/5))