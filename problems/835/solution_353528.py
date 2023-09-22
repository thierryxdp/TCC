def melhor_volta(matriz6x10):
    '''c'''
    resp=(0,min(0,0),0)
    for i in range(10):
        for j in range(6):
            if matriz6x10[i][j]!=resp[0]:
                resp=(i,min(matriz6x10[j]),j)
    return resp