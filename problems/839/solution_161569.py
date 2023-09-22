import math
def carros(pessoas,capacidade=5):
    '''função que calcula e retorna (em int), a quantidade necessária de
    carros para realizar uma viagem, tendo o número de pessoas (int),
    e a quantidade de assentos(int e se nao for informado = 5)'''
    return math.ceil(pessoas/capacidade)