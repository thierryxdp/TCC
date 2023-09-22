import math
def carros(pessoas , capacidade = 5):
    '''calcula o numero de carros para levar determinada quantidade de pessoas.'''
    return math.ceil(pessoas / 5)