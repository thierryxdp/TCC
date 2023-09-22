def carros(pessoas, capacidade=5):
	carros_necessarios = int(pessoas)//int(capacidade)
    if capacidade == 5:
        return carros_necessarios + 1
    return (carros_necessarios)