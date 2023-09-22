def carros(pessoas,capacidade=5):
    '''função que receve o numero de pessoas e a 
    capacidade do carro e retorna a quantidade de carros necessária'''
    import math.ceil
    return math.ceil(pessoas/capacidade)