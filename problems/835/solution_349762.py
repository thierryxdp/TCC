def melhor_volta(matriz6x10):
    menor_tempo = (0,0)
    melhorVolta = matriz6x10[0][0]
    for corredor in range(6):
        for volta in range(10):
            if matriz6x10[corredor][volta] < matriz6x10[melhorVolta[0]][melhorVolta[1]]:
                menor_tempo = min(matriz6x10[corredor][volta])
                volta_corredor = (corredor,volta)
    return (volta_corredor, menor_tempo)