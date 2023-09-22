def carros(passageiros,capacidade=5):
    '''Calcula a quantidade de carros necessária dada a quantidade de passageiros e a capacidade de cada veículo; int, int -> int'''
    return math.ceil(passageiros/capacidade)
import math ceil