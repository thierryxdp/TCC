def melhor_volta(matriz6x10):
    '''c'''
    resp=10000
    resp2=0
    for i in range(len(matriz6x10)):
        for j in range(len(matriz6x10[0])):
            if matriz6x10[i][j]<=resp:
                resp=matriz6x10[i][j]
                resp2=(i,(matriz6x10[i][j]),j)
    return resp2