def melhor_volta(matriz):
    tupla=()
    for i in range(len(matriz)):
        tupla=tupla+int(min(matriz[i]))
        for j in range(len(matriz[i])):
            tupla=tupla+int(min(matriz[i][j]))
            tupla=tupla+int(len(tempo))
    return tupla