def melhor_volta(matriz6x10):
    '''c'''
    resp=10000
    for i in range(len(matriz6x10)):
        for j in range(11):
            if matriz6x10[i][j]>=resp:
                resp=(i,min(matriz6x10[j]),j)
    return resp