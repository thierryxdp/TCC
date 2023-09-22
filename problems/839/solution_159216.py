import math
def carros (passageiros, capacidade=5):
    '''calcula e retorna o numero exato de carros necessarios para realizar uma viagem'''
    return math.ceil(passageiros/5)