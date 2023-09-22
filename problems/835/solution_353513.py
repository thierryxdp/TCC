def melhor_volta(matriz6x10):
    '''c'''
    resp=(0,min(0),0)
    for i in range(7):
        for j in range(11):
            if matriz6x10[i][j]<resp[1]:
                resp = (i,matriz_tempos[i][j],j)