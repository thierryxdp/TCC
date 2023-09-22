from math import ceil
def carros(pessoas,capacidade=5):
    '''Calcula o número de carros necessários em relação o número de pessoas. Caso
    a capacidade não seja dada ela será definida como 5'''
    
    return ceil(pessoas/capacidade)