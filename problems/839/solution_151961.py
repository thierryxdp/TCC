import math

def carros(p,c=5):
    '''calcula o numero de carros com capacidade c
    necessários para transportar p passageiros
    int->int'''
    return math.ceil(p/c)