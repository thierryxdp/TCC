import math
def carros(a,b=5):
    '''funcao que retorna o numero de carros necessarios para a viagem em funcao do numero de passageiros.'''
    return math.ceil(a/b)