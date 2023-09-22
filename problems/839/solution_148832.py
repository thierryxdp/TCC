from math import ceil
def carros (passageiros, capacidade=5):
    if passageiros < capacidade:
        if passageiros == 0:
        saida = 0
        saida = 1
    elif passageiros >= capacidade:
        saida = (passageiros // capacidade) + 1
    elif capacidade < 5:
        saida = passageiros // carro
    return saida