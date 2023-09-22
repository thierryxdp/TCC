def melhor_volta(matriz):
    checagem = 100
    for contador in range(6):
        for contagem in range(10):
            if matriz[contador][contagem] < checagem:
                voltas = (contador, matriz[contador][contagem], contagem)
	return voltas