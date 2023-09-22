def melhor_volta(matriz):
    tempo = 999999
    volta = 0
    corredor = 0
    for i in range(6):
        if min(matriz[i]) < tempo:
            tempo = min(matriz[i])
            volta = list.index(matriz[i], tempo)
            corredor = i + 1
    return (corredor, tempo, volta + 1)