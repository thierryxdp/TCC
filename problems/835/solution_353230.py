def melhor_volta(matriz_tempos):
    tupla = (0, float('inf'), 0)
    for x in range(6):
        for z in range(10):
            if matriz_tempos[x][z] < tupla[1]:
                tupla = (x + 1, matriz_tempos[x][z], z + 1) 
    return tupla