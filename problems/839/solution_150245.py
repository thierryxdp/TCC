import math

def carros(p,c=5):
    '''essa funcao retorna o numero exato de carros necessarios para uma viagem de acordo com as regras rodoviarias, dado como entrada o numero de pessoas para a viagem e a capacidade dos carros, considerando que todos os veiculos sao iguais'''
    return math.ceil(p/c)