def melhor_volta (matriz):
    '''Em uma corrida de Kart com 6 competidores em 10 voltas, a função retorna o campeão da melhor volta, seu melhor tempo e a volta campeã. 
    list -> tuple.'''
    campeao = 1
    tempo = 0
    volta = 1
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            tempo = min (matriz[i][j])
            if tempo < tempo -1:
                campeao = campeao + matriz[i]
                volta = volta + matriz [j]
    return (campeao,tempo,volta)