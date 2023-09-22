def melhor_volta(matriz):
    '''retorna a melhor volta em tempo da corrida'''
    tempo = matriz[0][0]
    for i in range (len(matriz)):
        tempoA = matriz[i]
        tempoB = min(tempoA)
        if tempoB <= tempo:
            tempo = tempoB
            tempoB = i
    volta_corrida = list.index(matriz[tempoB], tempo)
    return tempoB+1,tempo, volta_corrida +1