def melhor_volta(matriz):
    corredores = []
    tempo_corredor = []
    for linha in matriz:
        tempo = 1000000000
        volta = 0
        for elemento in linha:
            if elemento < tempo:
                tempo = elemento
                volta = linha.index(tempo)
		corredores.append((matriz.index(linha)+1,tempo, volta+1))
		tempo_corredor.append(tempo)
	melhor_tempo = min(tempo_corredor)
    for linha in corredores:
		for elemento in linha:
            if elemento == melhor_tempo:
                return linha