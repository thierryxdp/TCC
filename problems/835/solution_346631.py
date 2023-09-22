def melhor_volta(matriz):
    corredor = 0
    tempos = []
    listas = []
    
    for i in range(len(matriz)):
        tempo = 0
        for j in range(len(matriz[0])):
            tempo += matriz[i][j]
            listas += (i+1, tempo, j+1)
        list.append(tempos,tempo)
        
    
    melhor_tempo = min(tempos)
    
    return  listas[tempos.index(min(tempos)) + 1]