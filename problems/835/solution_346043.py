def melhor_volta(m):
    """essa função recebe uma matriz 6 x 10, e recebe uma tupla informando qual kart deu a maior volta;
    list->tuple"""
    y = (0,100,0)
    for v in range(1,6):
        for c in range(1,10):
            if matriz[v][c]<y[1]:
                y = (y + 1,matriz[v][c])
    return y