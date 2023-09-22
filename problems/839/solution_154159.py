import math
def carros(pessoas,lugares=5):
    '''função que define a quantidade necessária de carros
    para transportar um número de pessoas numa viagem'''
    return math.ceil(pessoas/lugares)