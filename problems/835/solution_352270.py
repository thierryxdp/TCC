def melhor_volta(matriz):
    "Retorna qual competidor obteve o melhor resultado"
    melhor_volta = 0
    tempo = 100000
    volta = 0
    for j in range(len(matriz[i])):
        if tempo > matriz [i][j]:
            tempo = matriz [i][j]
            melhor_volta = matriz [i].index(matriz[i][j])
            corredor = i+1
     return(corredor, tempo, melhor_volta)