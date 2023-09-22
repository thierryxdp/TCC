def melhor_volta(matriz):
    vencedor = 0
    tempo = 0
    volta = 0
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista += [matriz[i][j]]
    tempo = min(lista)
    vencedor = 0
    for i in range(len(matriz)):
        tempos_corredor = matriz[i]
        if tempo in tempos_corredor:
            vencedor = i
    volta = list.index(matriz[vencedor], tempo)
    return vencedor + 1, tempo, volta + 1