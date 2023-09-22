import math

def carros(pessoas, capacidade=5):
	carros_necessarios = pessoas//capacidade
    return math.ceil(carros_necessarios)