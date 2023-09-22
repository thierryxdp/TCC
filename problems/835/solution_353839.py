def melhor_volta(matriz):
    corredor1=matriz[0]
    corredor2=matriz[1]
    corredor3=matriz[2]
    corredor4=matriz[3]
    corredor5=matriz[4]
    corredor6=matriz[5]
    menores_tempos=[min(corredor1),min(corredor2),min(corredor3),min(corredor4),min(corredor5),min(corredor6)]
    menor_tempo=min(menores_tempos)
    for i in range(6):
        for j in range(10):
            if matriz[i][j]==menor_tempo:
                corredor=i+1
                volta=j+1
    return (corredor, menor_tempo,volta)