def carros(passageiros,capacidade=5):
    if passageiros//capacidade==passageiros/capacidade:
        return passageiros//capacidade
    else:
        return passageiros//capacidade+1