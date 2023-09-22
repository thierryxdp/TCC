def melhor_volta(matriz):
    melhor_tempo = []
    melhor_volta = []
    for linha in matriz:
        tempo = 10000
        volta = 0
        count = 0
        for elemento in linha:
            if elemento < tempo:
                tempo = elemento
                volta = count
        	count += 1
		melhor_tempo.append(tempo)
        melhor_volta.append(volta)
	melhor_corredor = melhor_tempo.index(min(melhor_tempo))
	return (melhor_corredor, min(melhor_tempo),melhor_volta[melhor_corredor])