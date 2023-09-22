def melhor_volta(matriz):
    checagem = 100
    tupla_voltas = ()
    for contador in range(6):
        for contagem in range(10):
            if matriz[contador][contagem] < checagem:
                tupla_voltas = (contador, matriz[contador][contagem], contagem[contador])
	return tupla_voltas