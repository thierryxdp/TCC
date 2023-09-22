def melhor_volta(matriz):
    tempo_corredor = []
    for linha in matriz:
        tempo = 0
        for elemento in linha:
            tempo += elemento
		tempo_corredor.append(tempo)
	return min(tempo_corredor)