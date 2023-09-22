import math
def carros (num_pessoas,cpcd=5):
    carros=math.ceil(num_pessoas/cpcd)
    '''
    funcao que calcula o numero exato de carros
    a partir do numero de pessoas e a capacidade
    dos carros 
    int,int->int
    '''
    return carros