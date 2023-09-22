def carros (passageiros, capacidade=5):
    '''calcule o numero de carros necessario para a viagem'''
    return math.ceil (passageiros/capacidade)