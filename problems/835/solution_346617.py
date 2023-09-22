def melhor_volta(matriz):
    corredor = 0
    tempos = []
    i = 0
    
    for i in range(len(matriz)):
        tempo = 0
        for j in range(len(matriz[0])):
            tempo += matriz[i][j]
        list.append(tempos,tempo)
    voltas = list.index(matriz[i],min(tempo))+1
    melhor_tempo = min(tempos)
    
    while min(tempo) not in matriz[i]:
         i = i +1
    corredor = i + 1
    
    return corredor, min(tempo), voltas