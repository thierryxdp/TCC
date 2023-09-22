def carros (pes,vag = 5):

    '''Calcula o número de carros necessários para realizar uma viagem baseado no número de pessoas e nas vagas disponíveis no carro'''

    # int, int -> int

    import math

    a = pes/vag

    return math.ceil (a)