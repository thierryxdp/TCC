def melhor_volta(matriz):
    linhas = 6
    colunas = 10
    melhorvolta0 = min(matriz[0])
    melhorvolta1 = min(matriz[1])
    melhorvolta2 = min(matriz[2])
    melhorvolta3 = min(matriz[3])
    melhorvolta4 = min(matriz[4])
    melhorvolta5 = min(matriz[5])
    melhorvoltageral = min(melhorvolta0, melhorvolta1, melhorvolta2, melhorvolta3, melhorvolta4, melhorvolta5)
    indice = 0
    for i in range(linhas):
        if melhorvoltageral in matriz[i]:
            corredor = i
            volta = list.index(matriz[i], melhorvoltageral)
    return (corredor + 1, melhorvoltageral, volta + 1)