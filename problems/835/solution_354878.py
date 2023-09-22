def melhor_volta(matriz):
    '''retorna a melhor volta em tempo da corrida'''
    tempo = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tempoA = min(matriz[j])
            if tempoA <= tempo:
                tempo = tempoA
                tempoA = i
    volta_corrida = list.index(matriz[tempoA], tempo)
    return tempoA+1, tempo, volta_corrida+1