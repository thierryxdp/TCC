def melhor_volta(matriz):
    tempo = 999999
    volta = 0
    corredor = 0
    for i in range(6):
        if min(matriz[i]) < tempo:
            tempo = min(matriz[i])
            volta = list.index(matriz[i], corredor)
            corredor = i
    return (corredor, tempo, volta)