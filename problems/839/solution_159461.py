import math
def carros(pessoas,capacidade=5):
    '''recebe o número de pessoas e a cpacidade do carro e retorna 
    a quantidade de carros necessários para transportar todo mundo; 
    se a capacidade não for informada a função considera ela igual a 5;
    int, int --> int'''
    return math.ceil(pessoas/capacidade)