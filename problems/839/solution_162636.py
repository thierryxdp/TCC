def carros(pessoas, capacidade=5):
	carros_necessarios = int(pessoas)//int(capacidade)
    if capacidade == 5:
        carros_necessarios = int(pessoas)//int(capacidade) + float(pessoas)%float(capacidade)
    return (carros_necessarios)