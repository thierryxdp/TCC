def melhor_volta(matriz6x10):
    '''c'''
    resp=(0,min(0,0),0)
    for i in range(6):
        for j in range(10):
            if matriz6x10[i][j]!=resp[0]:
                resp = (i,matriz6x10[i][j],j)
    return resp