def carros(pessoas, capacidade=5):
	carros_necessarios = pessoas//capacidade
    if capacidade > 5:
        return carros_necessarios + 1
    return round(carros_necessarios, 1)