def carros(pessoas,capacidade=5):
    '''função que calcula o número de carros necessários para realizar uma viagem dados o número de pessoas e a capacidade do carro;
    int -> int'''
    return math.ceil(pessoas/capacidade)