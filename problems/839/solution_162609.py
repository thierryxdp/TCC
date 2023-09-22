import math

def carros(pessoas, capacidade=5):
	carros_necessarios = pessoas//capacidade
    return ceil(carros_necessarios)