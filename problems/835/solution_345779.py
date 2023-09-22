def melhor_volta(matriz):
    tupla=()
    for i in range(6):
        for j in range(10):
            if matriz[i][j]<tupla[]:
                tupla=(i,matriz[i][j],j)
    return tupla