def melhor_volta(matriz):
    voltas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            voltas = voltas + matriz[i][j]
            if matriz[i][j] == min(voltas):
                corredor = i
                nvolta = j
    tempo = min(voltas)
    return corredor,tempo,nvolta