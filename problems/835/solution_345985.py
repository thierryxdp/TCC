def melhor_volta(matriz_tempos):
    """ Dunção que recebe matriz 6x10 com os tempos em segundos e retorna
    uma tupla.
    int-> float"""
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz_tempos[i][j] < tupla[1]:
                tupla = (i+1,matriz_tempos[i][j],j+1) 
    return tupla