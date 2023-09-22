import math
def bolos(A,B,C):
    '''
    Função que recebe o numero de cada ingrediente 
    para se fazer um bolo (onde "A" represneta as 
    xicaras de farinha de trigo, "B" o numero de ovos e
    "C" o numero de colheres de sopa de leite) e retorna o
    numero maximo de bolos que se pode fazer com dados 
    ingredientes( sabendo que 1 bolo é "A" =2 "B"=3 e "C"=5)
    int, int, int -> int
    '''
    return min(math.floor(A/2),math.floor(B/3),math.floor(C/5))