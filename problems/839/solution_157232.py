import math
def carros(passageiros, capacidade=5):
    ''' calcule a quantidade exata de carros para esta viagem. '''
    return math.ceil passageiros / capacidade