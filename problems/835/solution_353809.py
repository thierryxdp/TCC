def melhor_volta(matriz6x10):
    '''c'''
    resp=10000
    for i in range(7):
        for j in range(11):
            if matriz6x10[i][j]!=resp[0]:
                resp=(i,min(matriz6x10[j]),j)
    return resp