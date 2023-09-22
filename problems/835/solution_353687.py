def melhor_volta(matriz):
    tupla=()
    for i in range(len(matriz)):
        tupla=tupla+min(matriz[i])
        for j in range(len(matriz[i])):
            tupla=tupla+tempo=min(matriz[i][j])
            tupla=tupla+len(tempo)
    return tupla