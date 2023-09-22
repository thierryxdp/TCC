def melhor_volta(matriz):
	ts = []
    for tempos in matriz:
        for tempo in tempos:
            ts.append(tempo)  
    for i in range(9):
        for j in range(6):
            if min(ts) == matriz[j][i]:
    			jogador = j+1
                minimo = min(ts)
                volta = i+1
    return (jogador, minimo, volta)