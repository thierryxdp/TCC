def melhor_volta(matriz):
    """..."""
    tupla = (0)
    for i in range(matriz[6]):
        for j in range(matriz[10]):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1)
    return min(tupla)