def melhor_volta (matriz):
    '''Em uma corrida de Kart com 6 competidores em 10 voltas, a função retorna o campeão da melhor volta, seu melhor tempo e a volta campeã. 
    list -> tuple.'''
    tempo = matriz [0][0]
    volta = 1
    campeao = 1
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if tempo < matriz[i][j]:
                campeao = campeao + i
                volta = volta + j
                tempo = matriz[i][j]
    return (campeao,volta,tempo)