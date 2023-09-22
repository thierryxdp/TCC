def melhor_volta(matriz):
    melhor_tempo = [999999]
    for i in range(matriz):
        for h in range(matriz[i]):
        	if melhor_tempo > matriz[i][h]:
                melhor_tempo = matriz[i][h]
                volta = h
    return tuple(matriz[i], melhor_tempo, volta)