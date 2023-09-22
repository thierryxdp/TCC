def melhor_volta(matriz):
    tempo_corredor = []
    for linha in matriz:
        tempo = 10000
        volta = 0
        count = 0
        for elemento in linha:
            if elemento < tempo:
                tempo = elemento[count]
                volta = elemento
        	count += 1
		tempo_corredor.append(tempo)