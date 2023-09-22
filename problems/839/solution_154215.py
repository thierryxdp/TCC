import math
def carros(p,c=5):
    '''Função que calcula e retorna o número necessário de carros para a realização de uma viagem dados a quantidade de pessoas p e a capacidade do veículo c, a qual possui um valor padrão igual a 5
int,int --> int'''
    return math.ceil(p/c)