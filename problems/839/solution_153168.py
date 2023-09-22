def carros (passageiros, vagas=5):
    '''Calcula a quantidade de carros pra viagem dado o numero de passageiros'''
    import math
    return math.ceil (passageiros//vagas)