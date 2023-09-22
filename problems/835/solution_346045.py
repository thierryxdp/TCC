def melhor_volta(m):
    """essa função recebe uma matriz 6 x 10, e recebe uma tupla informando qual kart deu a maior volta;
    list->tuple"""
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j]<tupla[1]:
                tupla = (i + 1,matriz[i][j],j + 1)
    return tupla