def melhor_volta(matriz_tempo):
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz_tempo[i][j] < tupla[1]:
                tupla = (i+1,matriz_tempo[i][j],j+1)
    return tupla