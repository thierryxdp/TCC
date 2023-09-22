import math
def carros(passageiros,capacidade=5):
    '''Retorna a quantidade de carros necessários para realizar com a quantidade de
    	passageiros na viagem, alem da capacidade do carro, que caso nao seja convencional,
        deve ser expressa;
        int,int->int'''
    return math.ceil(passageiros/capacidade)