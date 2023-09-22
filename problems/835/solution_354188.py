def melhor_volta(matriz):

    melhorresultado=()
    melhorvolta = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < melhorvolta:
                melhorvolta = matriz[i][j] 
                melhorresultado = (i+1, melhorvolta, j+1)
    return melhorresultado