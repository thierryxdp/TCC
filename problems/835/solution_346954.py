def melhor_volta (matriz_t):
    """Funcao que recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e retorna uma tupla informando que foi a melhor volta"""
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz_t[i][j] < tupla[1]:
                tupla = (i+1, matriz_t[i][j], j+1)
    return tupla