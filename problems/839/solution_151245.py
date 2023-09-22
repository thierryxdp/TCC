def carros (passageiros, capacidade=5):
    '''calcule o numrto de carros necessario para a viagem'''
    return int math.ceil(passageiros/capacidade)