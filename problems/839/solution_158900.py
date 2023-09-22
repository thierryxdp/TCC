import math
def carros(pessoas,lugares=5):
    '''função que da a quantidade de carros que precisa para uma viagem em grupo, 
    a partir de quantas pessoas vão e a capacidade do carro.
    int,int -> int'''
    return math.ceil(pessoas/lugares)