def melhor_volta(matriz):
    corredor = 0
    tempos = []
    listas = []
    
    for i in range(len(matriz)):
        tempo = 0
        lista = 0
        for j in range(len(matriz[0])):
            tempo += matriz[i][j]
            lista += (i+1, tempo, j+1)
        list.append(tempos,tempo)
        list.append(listas,lista)
    
    melhor_tempo = min(tempos)
    
    return  listas[tempos.index(min(tempos)) + 1]