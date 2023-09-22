def melhor_volta(matriz):
    melhor_volta=0
    tempo=100000
    corredor=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if tempo > matriz[i][j]:
                tempo = matriz[i][j]
                melhor_volta = matriz[i].index(matriz[i][j])
                corredor = i+1
    return(corredor,tempo,melhor_volta)