def melhor_volta(matriz):
    tupla=()
    for i in range(len(matriz)):
        tupla=tupla+tuple(min(matriz[i]))
        for j in range(len(matriz[i])):
            tupla=tupla+tuple(min(matriz[i][j]))
            tupla=tupla+tuple(len(tempo))
    return tupla