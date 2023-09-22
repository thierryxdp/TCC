def melhor_volta(matriz):
    corredor =7
    volta = 11
    tempo = 6000
    for i in range(7):
        for j in range(11):
            tempo_volta = matriz[i][j]
            if (tempo_volta <= tempo):
                corredor = i
                volta = j
                tempo = tempo_volta
    return (corredor,tempo,volta)