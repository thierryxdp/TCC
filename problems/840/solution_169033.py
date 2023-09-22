from math import min
def bolos (A,B,C):
    ''' 
    funcao para calcular o numero de bolos dado o numero
    A de xicaras de farinhas de trigo, numero B de ovos e
    numero C de colheres de sopa de leite
    int,int ->int
    '''
    X = A/2
    Y = B/3
    Z = C/5
    return int(min(X,Y,Z))