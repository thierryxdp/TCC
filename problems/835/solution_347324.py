def melhor_volta(matriz):
    corredor = -1
    volta = -1
    tempo = 6000
    for i in range(6):
        for j in range(10):
            tempo_volta = matriz[i][j]
            if (tempo_volta <= tempo):
                corredor = i
                volta = j
                tempo = tempo_volta
    return ((corredor+1),tempo,(volta+1))