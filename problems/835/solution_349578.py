def melhor_volta(matriz):
    corredores = []
    for linha in matriz:
        melhor_tempo = 1000000000
        volta = 0
        for elemento in linha:
            if elemento < melhor_tempo:
                melhor_tempo = elemento
                volta = linha.index(melhor_tempo)
		corredores.append((matriz.index(linha),melhor_tempo, volta))
	return min(corredores)