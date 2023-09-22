def melhor_volta(matriz):
    corredores = []
    tempos = []
    voltas = []
    
    for i in range(len(matriz)):
        tempo = 0
        corredor = 0
        volta = 0
        for j in range(len(matriz[0])):
            corredor += i
            tempo += matriz[i][j]
            volta += j
        list.append(corredores,corredor)    
        list.append(tempos,tempo)
        list.append(voltas,volta)
        
    melhor_tempo = min(tempos)
    ganhador = corredores[tempos.index(min(tempos))+1]
    n = voltas[tempos.index(min(tempos))+1]
    
    return  ganhador , melhor_tempo, n