def melhor_volta(matriz):
    tupla= (0,float("inf"),0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j]<tupla[1]:
                tupla=(i+1,matriz[i][j],j+1)
    return tupla