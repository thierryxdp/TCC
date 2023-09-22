from math import ceil
def carros (passageiros,capacidade):
    '''funcao que calcula e retorna a quantidade de carros necessarios para uma viagem
    baseando-se na quantidade de passageiros e capacidade do veiculo como entradas'''
    return passageiros // capacidade