def melhor_volta(matriz):
    corredor = 0
    tempos = []
    
    for i in range(len(matriz)):
        tempo = 0
        for j in range(len(matriz[0])):
            tempo += matriz[i][j]
        list.append(tempos,tempo)
    
    melhor_tempo = min(tempos)
  	
    return melhor_tempo