#carros
import math
def carros(pessoas, capacidade=5):
    """funcao que calcula o numero exato de carros necessarios para uma viagem, dados o numero de pessoas e a capacidade do carro,  int, int => int"""
    return math.ceil(pessoas/capacidade)