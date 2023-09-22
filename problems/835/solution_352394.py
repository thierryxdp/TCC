def melhor_volta(matriz):
    melhor_volta=0
    tempo=10000
    corredor=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tempo = matriz[i][j]
            melhor_volta = matriz[i].index(j)+1
            corredor = i+1
    return(corredor,tempo,melhor_volta)