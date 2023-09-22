import math
def bolos(A,B,C):
    '''
    Essa função retorna o número (inteiro) de bolos que se faz com A xícaras de farinha,
    B ovos e C colheres de sopa de leite, onde para cada bolo é necessário 2 do ingrediente A,
    3 do B e 5 do C. 
    '''
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))