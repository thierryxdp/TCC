import math
def carros(pessoas,capacidade=5):
    '''Calcula e retorna o número de carros necessários para uma viagem
    dado o numero de pessoas e a capacidade dos carros (caso a capacidade
    seja maior que 5)(considerar todos carros de capacidade igual)'''
    return math.ceil((pessoas/capacidade))