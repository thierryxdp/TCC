def melhor_volta(matriz):
    checagem = []
    for contador in range(6):
        for contagem in range(10):
            if matriz[contador][contagem] < checagem:
                checagem = matriz[contador][contagem]
                voltas = (contador+1, matriz[contador][contagem], contagem+1)
	return voltas