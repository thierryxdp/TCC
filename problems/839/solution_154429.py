import math
def carros (pessoas, lugares=5):
    ''' Calcula a quantidade de carros é necessária dados os lugares (sendo o padrão 5 lugares) e a quantidade de pessoas'''
    return math.ceil (pessoas/lugares)