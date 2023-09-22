def carros(pessoas, capacidade=5):
	carros_necessarios = int(pessoas)//int(capacidade) + int(pessoas)%int(capacidade)
    return (carros_necessarios)