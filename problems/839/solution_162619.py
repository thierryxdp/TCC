def carros(pessoas, capacidade=5):
	carros_necessarios = pessoas//capacidade
    return round(carros_necessarios, 1)