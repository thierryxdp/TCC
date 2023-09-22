import math
def carros (passageiros, capacidade_carro):
    '''calcula e retorna o numero exato de carros para realizar uma viagem'''
    return math.ceil(passageiros/capacidade_carro)