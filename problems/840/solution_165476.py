import math
def bolos (a,b,c):
    '''
    Determina a quantidade de bolos máxima que João 
    consegue fazer
    Parâmetros: 
    		Entrada: a,b,c: int
            Saída: int
    '''
    return min (a/2,b/3,c/5)