def carros (passageiros,capacidade=5):
    '''calcular o numero de carros necessario para a viagem'''
    return int max(passageiros/capacidade)