def melhor_volta(matriz_tempos):
    """..."""
    tupla = 0
    for i in range(matriz_tempos[6]):
        for j in range(matriz_tempos[10]):
            if matriz_tempos[i][j] < tupla[1]:
                tupla = (i+1, matriz_tempos[i][j],j+1)
    return tupla