def melhor_volta(matriz):
    topvolta = 0
    for elemento in range(6):
        for time in range(10):
            if matriz[elemento][time] < topvolta[1]:
                topvolta = (1+elemento, matriz[elemento][tempo], time+1)
    return topvolta