from math import * 
def bolos(A,B,C):
    '''função que retorna a quantidade de bolos que João consegue fazer dados as medidas iniciais dos ingrediente
       int,int,int --> int '''
    
    q1 = floor(A/2)
    q2 = floor(B/3)
    q3 = floor(C/5)
    
    return min(q1,q2,q3)