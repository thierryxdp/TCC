import math

def carros(p,c=5):
    '''função para calcular o número de carros necessários para transportar
    p pessoas. Caso a capacidade de transporte seja diferente de 5, espera-
    se o valor de capacidade dos carros c'''
    return math.ceil(p/c)